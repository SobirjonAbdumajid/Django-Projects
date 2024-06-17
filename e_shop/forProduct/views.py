from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        category_name = request.data.get('category')

        # Check if the category exists
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return Response({'message': 'The specified category does not exist.'})

        # Update the request data with the category ID
        request.data['category'] = category.id

        name = request.data.get('name')
        if Products.objects.filter(name=name).exists():
            return Response({'message':'The product already exists.'})

        # Check if the product name already exists
        product_name = request.data.get('name')
        if Products.objects.filter(name=product_name).exists():
            return Response({'message': 'A product with this name already exists.'})

        # Proceed with serialization and saving the product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, **kwargs):
        if kwargs:
            id = self.kwargs.get('pk')
            obj = Category.objects.get(id=id)
            if not obj:
                return Response({'message': 'not found'})
            serializer = CategorySerializer(obj)
            return Response(serializer.data)

        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Products.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "product updated successfully!"})
        return Response(serializer.errors)



    def delete(self, request, **kwargs):
        product_id = self.kwargs.get('pk')
        product = Products.objects.get(id=product_id)
        if not product:
            return Response({'message': 'not found'})
        product.delete()
        return Response({'message':"Product deleted successfully!"})


class AddCategory(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        x_name = Category.objects.filter(name=name).first()
        if x_name:
            return Response({'message': 'this category already exists!'})
        obj = Category.objects.create(
            name=name,
            description=description,
        )
        serializer = CategorySerializer(obj)
        return Response(serializer.data)