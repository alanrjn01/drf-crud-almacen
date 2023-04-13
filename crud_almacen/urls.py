from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# https://drf-yasg.readthedocs.io/en/stable/readme.html#usage

schema_view = get_schema_view(
   openapi.Info(
      title="API Rest Almacen",
      default_version='v1',
      description='Documentación de los endpoints y modelos generados automáticamente por Swagger.',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('productos.urls')),
    path('api/',include('productos.api.routers')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

