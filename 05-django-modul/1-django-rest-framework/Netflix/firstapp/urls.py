from django.urls import path, include
from .views import MovieViewSet, ActorViewSet, AddCommentView, CommentListView, DeleteCommentView, MovieActorAPIView, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Movie application app",
        default_version='v1',
        description="This is the app description",
        contact=openapi.Contact(email='<sobirjon0305@gmail.com>'),
    ),
    public=True,
    permission_classes=(AllowAny,)
)


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

    # swagger and redoc
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),

    # Include the router URLs
    path('', include(router.urls)),

    # Movie-actor relationship endpoint
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),

    # Authentication endpoint
    path('auth/', obtain_auth_token),
]


# from django.urls import path, include
# from .views import MovieViewSet, ActorViewSet, AddCommentView, CommentListView, DeleteCommentView, MovieActorAPIView, CommentViewSet
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework.permissions import AllowAny
#
# # Initialize the router
# router = DefaultRouter()
# router.register(r'movies', MovieViewSet, basename='movie')
# router.register(r'actors', ActorViewSet, basename='actor')
# router.register(r'comment', CommentViewSet, basename='comment')
#
# # Set up schema view for Swagger and ReDoc
# schema_view = get_schema_view(
#     openapi.Info(
#         title="My API",
#         default_version='v1',
#         description="API documentation for the application",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="https://sobirjondev-portfolio.netlify.app/"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(AllowAny,),
# )
#
# urlpatterns = [
#     # Comment-related endpoints
#     path('comments/add/', AddCommentView.as_view(), name='add-comment'),
#     path('comments/list/', CommentListView.as_view(), name='list-comments'),
#     path('comments/delete/<int:id>/', DeleteCommentView.as_view(), name='delete-comment'),
#
#     # Include the router URLs
#     path('', include(router.urls)),
#
#     # Movie-actor relationship endpoint
#     path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),
#
#     # Authentication endpoint
#     path('auth/', obtain_auth_token),
#
#     # Swagger and ReDoc documentation endpoints
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]
