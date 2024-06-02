# from django.shortcuts import render
# from app1.models import Maqola
# # Create your views here.
# # -----------------------------------------------
#
# from .serializer import *
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Maqola
#
#
# @api_view(["POST"])
# def add_customer(request):
#     new_data = StuffSerializer(data=request.data)
#     if new_data.is_valid():
#         new_data.save()
#         return Response({"message": "Added Successfully"}, status=200)
#     return Response({"message": "Something went wrong!"}, status=400)
#
# @api_view(["GET"])
# def list_customer(request):
#     new_data = Maqola.objects.all()
#     new_data_json = StuffSerializer(new_data, many=True)
#     return Response(new_data_json.data)
#
# @api_view(["DELETE"])
# def customer_delete(request):
#     customer_id = request.data.get('id')
#     try:
#         xaridor = Maqola.objects.get(id=customer_id)
#         xaridor.delete()
#         return Response({"message": "Deleted Successfully"}, status=200)
#     except Maqola.DoesNotExist:
#         return Response({"message": "Customer not found!"}, status=404)
#
# @api_view(["PUT"])
# def customer_update(request):
#     customer_id = request.data.get('id')
#     try:
#         xaridor = Maqola.objects.get(id=customer_id)
#         xaridor.name = request.data.get('name', xaridor.name)
#         xaridor.surname = request.data.get('surname', xaridor.surname)
#         xaridor.age = request.data.get('age', xaridor.age)
#         xaridor.addres = request.data.get('addres', xaridor.addres)
#         xaridor.save()
#         return Response({"message": "Updated Successfully"}, status=200)
#     except Maqola.DoesNotExist:
#         return Response({"message": "Customer not found!"}, status=404)
#     except Exception as e:
#         return Response({"message": "Operation Failed"}, status=400)
#
# @api_view(["GET"])
# def customer_search(request):
#     try:
#         customer_title = request.query_params.get('title', '')
#         xaridor = Maqola.objects.filter(title__icontains=customer_title)
#         xaridor_json = StuffSerializer(xaridor, many=True)
#         return Response(xaridor_json.data)
#     except Exception as e:
#         return Response({"message": "Operation Failed"}, status=400)
#
#
# # -----------------------------------------------
# # @login_required()
# def maqola(request):
#     maqolalar = Maqola.objects.all().order_by('-id')
#     context = {
#         'maqolalar' : maqolalar
#     }
#     return render(
#         request=request,
#         template_name='maqola.html',
#         context=context
#     )
# # @login_required()
# def worldNews(request):
#     w_news = Maqola.objects.filter(tag='word').order_by('-id')
#     print(w_news)
#     context = {
#         'w_news' : w_news
#     }
#
#     return render(
#         request=request,
#         template_name='word.html',
#         context=context
#     )
# # @login_required()
# def local(request):
#     l_news = Maqola.objects.filter(tag='local').order_by('-id')
#     print(l_news)
#     context = {
#         'l_news' : l_news
#     }
#
#     return render(
#         request=request,
#         template_name='local.html',
#         context=context
#     )
# # @login_required()
# def sport(request):
#     s_news = Maqola.objects.filter(tag='sport').order_by('-id')
#     print(s_news)
#     context = {
#         's_news' : s_news
#     }
#
#     return render(
#         request=request,
#         template_name='sport.html',
#         context=context
#     )
#
# def article_detail(request, id):
#     maqola = Maqola.objects.get(id=id)
#     context = {
#         'maqola':maqola
#     }
#
#     return render(
#         request=request,
#         template_name='article_detail.html',
#         context=context,
#     )
from django.shortcuts import render
from .models import Maqola
from .serializer import StuffSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def add_customer(request):
    new_data = StuffSerializer(data=request.data)
    if new_data.is_valid():
        new_data.save()
        return Response({"message": "Added Successfully"}, status=200)
    return Response({"message": "Something went wrong!"}, status=400)


@api_view(["GET"])
def list_customer(request):
    new_data = Maqola.objects.all()
    new_data_json = StuffSerializer(new_data, many=True)
    return Response(new_data_json.data)


@api_view(["DELETE"])
def customer_delete(request):
    customer_id = request.data.get('id')
    try:
        xaridor = Maqola.objects.get(id=customer_id)
        xaridor.delete()
        return Response({"message": "Deleted Successfully"}, status=200)
    except Maqola.DoesNotExist:
        return Response({"message": "Customer not found!"}, status=404)


@api_view(["PUT"])
def customer_update(request):
    customer_id = request.data.get('id')
    try:
        xaridor = Maqola.objects.get(id=customer_id)
        xaridor.name = request.data.get('name', xaridor.name)
        xaridor.surname = request.data.get('surname', xaridor.surname)
        xaridor.age = request.data.get('age', xaridor.age)
        xaridor.address = request.data.get('address', xaridor.address)
        xaridor.rank = request.data.get('rank', xaridor.rank)
        xaridor.tag = request.data.get('tag', xaridor.tag)
        xaridor.save()
        return Response({"message": "Updated Successfully"}, status=200)
    except Maqola.DoesNotExist:
        return Response({"message": "Customer not found!"}, status=404)
    except Exception as e:
        return Response({"message": "Operation Failed"}, status=400)


@api_view(["GET"])
def customer_search(request):
    try:
        customer_name = request.query_params.get('name', '')
        xaridor = Maqola.objects.filter(name__icontains=customer_name)
        xaridor_json = StuffSerializer(xaridor, many=True)
        return Response(xaridor_json.data)
    except Exception as e:
        return Response({"message": "Operation Failed"}, status=400)


# Non-API views
def maqola(request):
    maqolalar = Maqola.objects.all().order_by('-id')
    context = {'maqolalar': maqolalar}
    return render(request, 'maqola.html', context)

def worldNews(request):
    w_news = Maqola.objects.filter(tag='world').order_by('-id')
    context = {'w_news': w_news}
    return render(request, 'word.html', context)

def local(request):
    l_news = Maqola.objects.filter(tag='local').order_by('-id')
    context = {'l_news': l_news}
    return render(request, 'local.html', context)

def sport(request):
    s_news = Maqola.objects.filter(tag='sport').order_by('-id')
    context = {'s_news': s_news}
    return render(request, 'sport.html', context)

def article_detail(request, id):
    maqola = Maqola.objects.get(id=id)
    context = {'maqola': maqola}
    return render(request, 'article_detail.html', context)
