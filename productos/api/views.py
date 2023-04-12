from rest_framework import generics
from productos.models import Categoria
from productos.api import serializers
from productos.base.base_api_views import BaseListApiView,BaseCreateApiView

#ListApiView solamente reconoce la informacion que proviene por el metodo get
#le pasa la consulta al serializador definido e internamente retorna un Response

#Categoria
class CategoriaListApiView(generics.ListAPIView):
    #serializador en cual toma la referencia
    serializer_class = serializers.CategoriaSerializer
    
    #consulta especificada
    def get_queryset(self):
        categoria = Categoria.objects.filter()
        return categoria
    
class CategoriaCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.CategoriaSerializer
    
    
#utilizando jerarquia de clases:    
#-----------
#Producto    
class ProductoListApiView(BaseListApiView):
    serializer_class = serializers.ProductoSerializer
    
    
class ProductoCreateApiView(BaseCreateApiView):
    serializer_class = serializers.ProductoSerializer
    
#-----
#Sucursal
    
class SucursalListApiView(BaseListApiView):
    
    serializer_class = serializers.SucursalSerializer
    
class SucursalCreateApiView(BaseCreateApiView):
    
    serializer_class = serializers.SucursalSerializer
    
#--------   
#Producto_Sucursal    
class Producto_SucursalListApiView(BaseListApiView):
    
    serializer_class = serializers.Producto_SucursalSerializer
    
class Producto_SucursalCreateApiView(BaseCreateApiView):
    
    serializer_class = serializers.Producto_SucursalSerializer

