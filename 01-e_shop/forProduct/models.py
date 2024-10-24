from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_price(self):
        return self.price

