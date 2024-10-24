# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from .serializers import OrderSerializer, OrderDetailSerializer
# from .models import OrderDetail, Order
#
#
# # class CreateOrderAPIView(APIView):
# #     permission_classes = [permissions.AllowAny]
# #     def post(self, request):
# #         # This handles the Order creation
# #         order_data = {
# #             'customer': request.data.get('customer'),
# #             'status': request.data.get('status', 'pending')
# #         }
# #         order_serializer = OrderSerializer(data=order_data)
# #
# #         if order_serializer.is_valid():
# #             order = order_serializer.save()
# #
# #             # This handles OrderDetails creation
# #             order_details = request.data.get('details', [])
# #             details_responses = []
# #             for detail in order_details:
# #                 detail_data = {
# #                     'order': order.id,
# #                     'product': detail.get('product'),
# #                     'quantity': detail.get('quantity'),
# #                     'price': detail.get('price')
# #                 }
# #                 detail_serializer = OrderDetailSerializer(data=detail_data)
# #                 if detail_serializer.is_valid():
# #                     detail_serializer.save()
# #                     details_responses.append(detail_serializer.data)
# #                 else:
# #                     return Response(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #             response_data = {
# #                 'order': order_serializer.data,
# #                 'order_details': details_responses
# #             }
# #             return Response(response_data, status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class OrderAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# #
# #     def get(self, request):
# #         orders = Order.objects.all()
# #         serializer = OrderSerializer(orders, many=True)
# #         return Response(serializer.data)
#
# # class OrderDetailAPIView(APIView):
# #     permission_classes = [permissions.AllowAny]
# #     def get(self, request):
# #         order_detail = OrderDetail.objects.all()
# #         serializer = OrderSerializer(order_detail, many=True)
# #         return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import OrderSerializer, OrderDetailSerializer
from .models import OrderDetail

# class OrderAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Add(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OrderAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        order_detail = OrderDetail.objects.get(pk=pk)
        serializer = OrderDetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)