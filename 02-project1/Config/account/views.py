from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password # make_password -> heshlab yuklaydi. check_password -> heshlangan funksiyani tekshiradi
from .decorators import authenticated


# Create your views here.
@authenticated
def register(request):
    if request.method == 'POST':
        # print(request.POST)
        email = request.POST.get('email')
        name = request.POST.get('first_name')
        surename = request.POST.get('second_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user = CustomUser.objects.filter(email=email).first() # CustomUser.objects -> mana shu email bormi tekshiradi. first -> usha oladi emailni
        if ex_user:
            return HttpResponse('<h1>Email already registered!</h1>')
        elif password1 != password2 or password2 is None or password1 is None:
            return HttpResponse('<h1>Parollarni to\'g\'ri kiriting.</h1>')
        else:
            user = CustomUser.objects.create_user(
                email=email,
                first_name=name,
                last_name=surename,
                password=make_password(password1),
            )

            login(request=request, user=user)
            return redirect('maqola')

    return render(
        request=request,
        template_name='auth/register.html'
    )

@authenticated
def log_in(request):
    # if request.user.is_authenticated:
    #     return redirect('maqola')
    if request.method == 'POST':
        # print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email, password)
        user = authenticate(request, email=email, password=password) # authenticate databasedan borib shu email bormi yo'qmi tekshiradi
        if user:
            login(request=request, user=user)
            return redirect('maqola')
        else:
            return HttpResponse('<h1>Invalid Credentials!</h1>')
    return render(
        request=request,
        template_name = 'auth/login.html'
    )

def log_out(request):
    logout(request)
    return redirect('maqola')

# def find_email(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         user = CustomUser.objects.filter(email=email).first()
#         if user:
#             print(user.email)  # Print the user's email if found
#             return HttpResponse(f"User email: {user.email}")
#         else:
#             print("We could not find your email")  # Print a message if email not found
#             return HttpResponse("We could not find your email")
#
#     return HttpResponse("Please make a POST request to check for an email.")


# def forget_password(request):
#     # if request.user.is_authenticated:
#     #     return redirect('maqola')
#     if request.method == 'POST':
#         # print(request.POST)
#         email = request.POST.get('email')
#         # password = request.POST.get('password')
#         # print(email, password)
#         user = authenticate(request, email=email) # authenticate databasedan borib shu email bormi yo'qmi tekshiradi
#         if not user:
#             # login(request=request, user=user)
#             return render('<h1>A code will be sent to your email account</h1>', email)
#         else:
#             return HttpResponse('<h1>Invalid Credentials!</h1>')
#     return render(
#         request=request,
#         template_name = 'auth/change_password.html'
#     )
# def forget_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         user = CustomUser.objects.filter(email=email)
#         if user:
#             # Generate a password reset token
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))

#             # Construct the password reset link
#             reset_link = f"{settings.BASE_URL}/reset_password/{uid}/{token}/"

#             # Send the password reset link to the user's email
#             send_mail(
#                 'Password Reset Link',
#                 f'Click the following link to reset your password: {reset_link}',
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False,
#             )
#             return HttpResponse('A link will be sent to your email, open the forget password page from there!')
#         else:
#             return HttpResponse('Invalid email address!')

#     return render(
#         request=request,
#         template_name='auth/change_password.html'
#     )

# def forget_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         user = CustomUser.objects.filter(email=email).first()
#         if user:
#             # Generate a password reset token
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#
#             # Construct the password reset link
#             reset_link = f"{settings.BASE_URL}/reset_password/{uid}/{token}/"
#
#             # Send the password reset link to the user's email
#             send_mail(
#                 'Password Reset Link',
#                 f'Click the following link to reset your password: {reset_link}',
#                 settings.EMAIL_HOST_USER,
#                 [email],
#                 fail_silently=False,
#             )
#             return HttpResponse('A link will be sent to your email, open the forget password page from there!')
#         else:
#             return HttpResponse('Invalid email address!')
#
#     return render(
#         request=request,
#         template_name='auth/change_password.html'
#     )