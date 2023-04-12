from rest_framework import serializers #importo los serializadores
from productos.models import Categoria,Producto,Producto_Sucursal,Sucursal #importo la clase del modelo


#creo un serializer del modelo a partir de la clase ModelSerializer
class CategoriaSerializer(serializers.ModelSerializer):
    
    #indico los metadatos del serializer
    # model = modelo de django
    # fields = '__all__' para mostrar todos los campos
    # exclude = los campos a excluir en las consultas
    class Meta:
        model = Categoria
        exclude = ('fecha_creacion',)
        
        
class ProductoSerializer(serializers.ModelSerializer):

    #usando stringrelatedfield, en los formularios de django no vas a poder tener autocompletado
    categoria_id = serializers.StringRelatedField()

    class Meta:
        model = Producto
        exclude = ('fecha_creacion',)
        
        
class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        exclude = ('fecha_creacion',)
        
        
class Producto_SucursalSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Producto_Sucursal
        fields = '__all__'
