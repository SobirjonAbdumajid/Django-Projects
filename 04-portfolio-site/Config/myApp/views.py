from django.shortcuts import render
from .models import MaqolaModel
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .serializer import MySerializer
from rest_framework.response import Response
from django.core.paginator import Paginator

from .filters import ProjectFilter
#
# def projects(request):
#     queryset = MaqolaModel.objects.filter(tags='Projects').order_by('-id')
#     filterset = ProjectFilter(request.GET, queryset=queryset)
#     context = {
#         'filterset': filterset
#     }
#     return render(
#         request=request,
#         template_name='sport.html',
#         context=context,
#     )

def projects(request):
    queryset = MaqolaModel.objects.filter(tags='Projects').order_by('-id')
    filterset = ProjectFilter(request.GET, queryset=queryset)
    context = {
        'filterset': filterset
    }
    return render(
        template_name='sport.html',
        request=request,
        context=context,
    )
# # Create your views here.

def home(request):
    certificates = MaqolaModel.objects.filter(tags="Certificates").order_by('-id')
    projects = MaqolaModel.objects.filter(tags='Projects').order_by('-id')
    education = MaqolaModel.objects.filter(tags='Education').order_by('-id')
    context = {
        'certificates':certificates,
        'projects':projects,
        'education':education,
    }
    return render(
        request=request,
        template_name='maqola.html',
        context=context,
    )

# @login_required
def certificates(request):
    certificates = MaqolaModel.objects.filter(tags="Certificates").order_by('-id')

    somsa = Paginator(MaqolaModel.objects.filter(tags="Certificates").order_by('-id'), 1)
    page = request.GET.get('page')
    vanues = somsa.get_page(page)

    context = {
        'certificates':certificates,
        'somsa':somsa,
        'vanues':vanues,
    }
    return render(
        request=request,
        template_name='world.html',
        context=context,

    )

# def projects(request):
#     projects = MaqolaModel.objects.filter(tags='Projects').order_by('-id')
#     context = {
#         'projects':projects
#     }
#     return render(
#         request=request,
#         template_name='sport.html',
#         context=context,
#     )

def education(request):
    education = MaqolaModel.objects.filter(tags='Education').order_by('-id')
    context = {
        'education':education
    }
    return render(
        request=request,
        template_name='local.html',
        context=context,
    )

def article_details(request, id):
    maqola = MaqolaModel.objects.get(id=id)
    context = {
        'maqolalar':maqola
    }
    return render(
        request=request,
        template_name='article_details.html',
        context=context,
    )

@api_view(['POST'])
def add(request):
    new_info = MySerializer(data=request.data)
    if new_info.is_valid():
        new_info.save()
        return Response({'message': 'Added successfully'}, status=200)
    return Response({'message':'Something went wrong'}, status=400)


@api_view(['GET'])
def list(request):
    all_projects = MaqolaModel.objects.all()
    all_projects_json = MySerializer(all_projects, many=True)
    return Response(all_projects_json.data)


@api_view(['DELETE'])
def delete(request):
    info_id = request.data.get('id')
    try:
        info = MaqolaModel.objects.get(id=info_id)
        info.delete()
        return Response('Deleted successfully', status=200)
    except MaqolaModel.DoesNotExist:
        return Response('Information does not exist', status=404)


@api_view(['PUT'])
def update(request):
    info_id = request.data.get('id')
    try:
        info = MaqolaModel.objects.get(id=info_id)
        info.title = request.data.get('title', info.title)
        info.image = request.data.get('image', info.image)
        info.source = request.data.get('source', info.source)
        info.link = request.data.get('link', info.link)
        info.description_eng = request.data.get('description_eng', info.description_eng)
        info.description_uzb = request.data.get('description_uzb', info.description_uzb)
        info.tags = request.data.get('tags', info.tags)
        info.save()
        return Response({"message":'Updated successfully'}, status=200)
    except MaqolaModel.DoesNotExist:
        return Response({"message": "Customer not found!"}, status=404)
    except Exception as e:
        return Response({"message": ["Operation Failed", e]}, status=400)

@api_view(['GET'])
def search(request):
    try:
        info_title = request.query_params.get('title')
        info = MaqolaModel.objects.filter(title__icontains=info_title)
        info_json = MySerializer(info, many=True)  # Serialize the queryset
        return Response(info_json.data)  # Return the serialized data
    except Exception as e:
        print(f"Search operation failed: {e}")  # Print the exception
        return Response({"message": "Operation Failed"}, status=400)