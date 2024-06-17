from rest_framework import serializers
from .models import Order, OrderDetail, Products

class OrderDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity', 'price']

    def get_price(self, obj):
        return obj.product.price * obj.quantity # Assuming your Products model has a 'price' field

class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'status', 'total_price', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        order = Order.objects.create(**validated_data)
        total_price = 0

        for detail_data in details_data:
            product = Products.objects.get(id=detail_data['product'].id)
            price = product.price  # Get the price from the product model
            quantity = detail_data.get('quantity', 1)
            total_price += price * quantity
            OrderDetail.objects.create(order=order, product=product, quantity=quantity, price=price)

        order.total_price = total_price
        order.save()
        return order



# from rest_framework import serializers
# from .models import Order, OrderDetail, Products
#
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['customer', 'status']
#
# class OrderDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDetail
#         fields = ['order', 'product', 'quantity', 'price']
#
#     def validate(self, attrs):
#         # Ensure the product exists and fetch its price
#         try:
#             product = Products.objects.get(pk=attrs['product'].id)
#         except Products.DoesNotExist:
#             raise serializers.ValidationError("The specified product does not exist.")
#
#         # Calculate the price based on quantity
#         attrs['price'] = product.price * attrs['quantity']
#         return attrs
#
#     def create(self, validated_data):
#         # Create the OrderDetail instance with the calculated price
#         return OrderDetail.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         # Update the OrderDetail instance and recalculate the price if necessary
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.product = validated_data.get('product', instance.product)
#         instance.price = instance.product.price * instance.quantity
#         instance.save()
#         return instance