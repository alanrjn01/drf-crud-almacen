from django.urls import path
from .api import views

#las vistas las retornamos como .as_view()
urlpatterns = [
    path('categoria/',views.CategoriaListApiView.as_view(),name='categoria'),
    path('categoria/create',views.CategoriaCreateApiView.as_view(),name='categoria_create'),
    path('producto/',views.ProductoListApiView.as_view(),name='producto'),
    path('producto/create',views.ProductoCreateApiView.as_view(),name='producto_create'),
    path('sucursal/',views.SucursalListApiView.as_view(),name='sucursal'),
    path('sucursal/create',views.SucursalCreateApiView.as_view(),name='sucursal_create'),
    path('producto_sucursal/',views.Producto_SucursalListApiView.as_view(),name='producto_sucursal'),
    path('producto_sucursal/create',views.Producto_SucursalCreateApiView.as_view(),name='producto_sucursal_create')
]
