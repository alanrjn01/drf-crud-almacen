from django.urls import path
from .api import views

#las vistas las retornamos como .as_view()
urlpatterns = [
    path('categoria/',views.CategoriaListApiView.as_view(),name='categoria'),
    path('categoria/create/',views.CategoriaCreateApiView.as_view(),name='categoria_create'),
    path('categoria/retrieve/<int:pk>/',views.CategoriaRetrieveApiView.as_view(),name='categoria_retrieve'),
    path('categoria/update/<int:pk>/',views.CategoriaUpdateApiView.as_view(),name='categoria_update'),
    path('categoria/destroy/<int:pk>/',views.CategoriaDestroyApiView.as_view(),name='categoria_destroy'),
    path('producto/',views.ProductoListCreateApiView.as_view(),name='producto'),
    path('producto/<int:pk>/',views.ProductoRetrieveUpdateDestroyApiView.as_view(),name='producto_retrieve_update_delete'),
    path('sucursal/',views.SucursalListCreateApiView.as_view(),name='sucursal'),
    path('sucursal/<int:pk>/',views.SucursalRetrieveUpdateDestroyApiView.as_view(),name='sucursal_retrieve_update_delete'),
    path('producto_sucursal/',views.ProductoSucursalListCreateApiView.as_view(),name='producto_sucursal'),
    path('producto_sucursal/<int:pk>/',views.ProductoSucursalRetrieveUpdateDestroyApiView.as_view(),name='productosucursal_retrieve_update_delete')
]
