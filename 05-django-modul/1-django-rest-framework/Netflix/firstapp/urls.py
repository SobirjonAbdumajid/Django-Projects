# from django.urls import path, include
# from .views import MovieViewSet
# from .views import AddCommentView, CommentListView, DeleteCommentView
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
#
# from .views import MovieViewSet, ActorViewSet, MovieActorAPIView
#
# router = DefaultRouter()
# router.register(r'movies', MovieViewSet)
# router.register(r'actors', ActorViewSet)
# router.register(r'comment', ActorViewSet)
#
# urlpatterns = [
#     # path('movies/', MovieAPIView.as_view(), name='movie'),
#     # path('actor/', ActorAPIView.as_view(), name='actor'),
#     path('comments/add/', AddCommentView.as_view(), name='add-comment'),
#     path('comments/list/', CommentListView.as_view(), name='list-comments'),
#     path('comments/delete/<int:id>/', DeleteCommentView.as_view(), name='delete-comment'),
#     path('', include(router.urls)),
#     path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),
#     path('auth/', obtain_auth_token),
# ]
#
# """
#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from todo.views import TodoViewSet
# from rest_framework.authtoken.views import obtain_auth_token
#
#
# router = DefaultRouter()
# router.register('todo', TodoViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('auth/', obtain_auth_token)
# ]
#
#
# """


from django.urls import path, include
from .views import MovieViewSet, ActorViewSet, AddCommentView, CommentListView, DeleteCommentView, MovieActorAPIView, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Initialize the router
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    # Comment-related endpoints
    path('comments/add/', AddCommentView.as_view(), name='add-comment'),
    path('comments/list/', CommentListView.as_view(), name='list-comments'),
    path('comments/delete/<int:id>/', DeleteCommentView.as_view(), name='delete-comment'),

    # Include the router URLs
    path('', include(router.urls)),

    # Movie-actor relationship endpoint
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),

    # Authentication endpoint
    path('auth/', obtain_auth_token),
]
