# # # # # from django.db import models
# # # # # from django.conf import settings
# # # # # from forProduct.models import Products
# # # # # from app.models import CustomUser
# # # # #
# # # # # # Create your models here.
# # # # # class Order(models.Model):
# # # # #     customer = models.ForeignKey(CustomUser, related_name='users', on_delete=models.CASCADE)
# # # # #     created_at = models.DateTimeField(auto_now_add=True)
# # # # #     updated_at = models.DateTimeField(auto_now=True)
# # # # #     status = models.CharField(max_length=33)  # Example statuses: pending, completed, cancelled
# # # # #
# # # # #
# # # # #     def __str__(self):
# # # # #         return f'Order {self.id} - {self.status}'
# # # # #
# # # # # class OrderDetail(models.Model):
# # # # #     order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
# # # # #     product = models.ForeignKey(Products, on_delete=models.CASCADE)
# # # # #     quantity = models.IntegerField(default=1)
# # # # #     price = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming price is per unit
# # # # #
# # # # #     def __str__(self):
# # # # #         return f'{self.quantity} ta {self.product.name}'
# # # # from django.db import models
# # # # import uuid
# # # #
# # # # class Order(models.Model):
# # # #     id = models.AutoField(primary_key=True)
# # # #     user_id = models.UUIDField(default=uuid.uuid4, editable=False)
# # # #     total_price = models.DecimalField(max_digits=10, decimal_places=2)
# # # #     status = models.CharField(max_length=20, default='pending')
# # # #     created_at = models.DateTimeField(auto_now_add=True)
# # # #     updated_at = models.DateTimeField(auto_now=True)
# # # #
# # # #     def __str__(self):
# # # #         return f'Order {self.id} - {self.status}'
# # # #
# # # # class OrderDetail(models.Model):
# # # #     id = models.AutoField(primary_key=True)
# # # #     order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
# # # #     product_id = models.UUIDField(default=uuid.uuid4, editable=False)
# # # #     quantity = models.IntegerField()
# # # #     price = models.DecimalField(max_digits=10, decimal_places=2)
# # # #
# # # #     def __str__(self):
# # # #         return f'{self.quantity} of Product ID {self.product_id}'
# # # from django.db import models
# # # from django.conf import settings
# # # from forProduct.models import Products
# # # from app.models import CustomUser
# # #
# # # class Order(models.Model):
# # #     customer = models.ForeignKey(
# # #         CustomUser,
# # #         related_name='orders',  # Changed from 'users' to 'orders' for clarity
# # #         on_delete=models.CASCADE
# # #     )
# # #     created_at = models.DateTimeField(auto_now_add=True)
# # #     updated_at = models.DateTimeField(auto_now=True)
# # #     status = models.CharField(
# # #         max_length=33,
# # #         default='pending'  # Consider adding a default status
# # #     )
# # #
# # #     def __str__(self):
# # #         return f'Order {self.id} - {self.status}'
# # #
# # # class OrderDetail(models.Model):
# # #     order = models.ForeignKey(
# # #         Order,
# # #         related_name='details',
# # #         on_delete=models.CASCADE
# # #     )
# # #     product = models.ForeignKey(
# # #         Products,
# # #         on_delete=models.CASCADE
# # #     )
# # #     quantity = models.IntegerField(default=1)
# # #     price = models.DecimalField(
# # #         max_digits=10,
# # #         decimal_places=2  # Ensure this matches the expected price scale
# # #     )
# # #
# # #     def __str__(self):
# # #         return f'{self.quantity} ta {self.product.name}'
# # from django.db import models
# # import uuid
# #
# # class Order(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     user_id = models.UUIDField(default=uuid.uuid4, editable=False)
# #     total_price = models.DecimalField(max_digits=10, decimal_places=2)
# #     status = models.CharField(max_length=20, default='pending')
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)
# #
# #     def __str__(self):
# #         return f'Order {self.id} - {self.status}'
# #
# # class OrderDetail(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
# #     product_id = models.UUIDField(default=uuid.uuid4, editable=False)
# #     quantity = models.IntegerField()
# #     price = models.DecimalField(max_digits=10, decimal_places=2)
# #
# #     def __str__(self):
# #         return f'{self.quantity} of Product ID {self.product_id}'
#
# from django.db import models
# from django.conf import settings
# from forProduct.models import Products
#
# class Order(models.Model):
#     customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=20, default='pending')  # Example statuses: pending, completed, cancelled
#
#     def __str__(self):
#         return f'Order {self.id} - {self.status}'
#
# class OrderDetail(models.Model):
#     order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming price is per unit
#
#     def __str__(self):
#         return f'{self.quantity} of {self.product.name}'


from django.db import models
from forProduct.models import Products
from app.models import CustomUser


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=33)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Order id: {self.id},  {self.customer}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.quantity} ta {self.product.name}'
