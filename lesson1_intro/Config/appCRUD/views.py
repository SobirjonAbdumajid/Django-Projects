from .models import Customer
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def add_customer(request):
    new_data = CustomerSerializer(data = request.data)
    if new_data.is_valid():
        new_data.save()
        return Response({"message: ": "Added Successfully"}, status = 200)
    return Response({"message: ": "Something went wrong!"}, status=400)

@api_view(["GET"])
def list_customer(request):
    new_data = Customer.objects.all()
    new_data_json = CustomerSerializer(new_data, many=True)
    return Response(new_data_json.data)

@api_view(["DELETE"])
def customer_delete(request):
    xaridor = Customer.objects.all()
    customer = request.data
    customer_id = customer.get('id')
    xaridor = Customer.objects.get(id = customer_id)
    xaridor.delete()
    return Response({"message: ": "Deleted Successfully"}, status = 200)

@api_view(["PUT"])
def customer_update(request):
    try:
        customer = request.data
        customer_id = customer.get('id')
        xaridor = Customer.objects.get(id = customer_id)
        xaridor.name=customer.get('name')
        xaridor.surname=customer.get('surname')
        xaridor.age=customer.get('age')
        xaridor.addres = customer.get('addres')
        xaridor.save()
        return Response({"message: ": "Updated Successfully"}, status = 200)
    except Exception as e:
        return Response({"message: ": "Operation Failed"}, status = 400)

@api_view(["GET"])
def customer_search(request):
    try:
        customer = request.data
        customer_name = customer.get('name')
        # customer_surname = customer.get('surname')
        xaridor = Customer.objects.filter(name__icontains = customer_name)
        xaridor_json = CustomerSerializer(xaridor, many=True)
        return Response(xaridor_json.data)
    except:
        return Response({"message: ": "Operation Failed"}, status = 400)
