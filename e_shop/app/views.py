from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import CustomUser, CodeConfirmation
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from helpers import code_token, send_code, code_4

class RegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        x_user = CustomUser.objects.filter(email=email).first()
        if x_user:
            return Response({"massage": "this email is already registered"})

        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=True,
        )

        token = RefreshToken.for_user(user)
        return Response({
            'message': 'Registered successfully',
            'user': UserSerializer(user).data,
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        })

class LoginStart(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        code_t = code_token.generate_code_token()
        code = code_4.generate_code()
        send_code.send_email(email, code)
        CodeConfirmation.objects.create(
            user=user,
            code=code,
            code_token=code_t
        )

        if user is not None:
            if user.is_active:
                return Response({
                    'message': 'email sent',
                    'code_token': code_t,
                })
            else:
                return Response({'message': 'Account is not active'})
        else:
            return Response({'message': 'Invalid credentials'})

class LoginEnd(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        code = request.data.get('code')
        code_t = request.data.get('code_t')

        code_confirm = CodeConfirmation.objects.filter(code_token=code_t).first()
        if not code_confirm:
            return Response({'message': 'Invalid token'})

        if code_confirm.code == int(code):
            user = code_confirm.user
            if user and user.is_active:
                token = RefreshToken.for_user(user)
                code_confirm.delete()

                return Response({
                    'message': 'Verification successful',
                    # 'user': UserSerializer(user).data,
                    'access_token': str(token.access_token),
                    'refresh_token': str(token),
                })
            else:
                return Response({'message': 'User not found or inactive'})
        else:
            return Response({'message': 'Invalid verification code'})

# class AddProductAPIView(APIView):
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
