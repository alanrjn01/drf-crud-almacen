from rest_framework import serializers #importo los serializadores
from productos.models import Categoria,Producto,Producto_Sucursal,Sucursal #importo la clase del modelo


#creo un serializer del modelo a partir de la clase ModelSerializer
class CategoriaSerializer(serializers.ModelSerializer):
    
    #Swagger toma los metadatos para realizar la documentacion, no el metodo to_representation()
    
    #indico los metadatos del serializer
    # model = modelo de django
    # fields = '__all__' para mostrar todos los campos
    # exclude = los campos a excluir en las consultas
    class Meta:
        model = Categoria
        exclude = ('fecha_creacion',)
        
        
class ProductoSerializer(serializers.ModelSerializer):

    #usando stringrelatedfield, en los formularios de django no vas a poder tener autocompletado
    #categoria_id = serializers.StringRelatedField()

    class Meta:
        model = Producto
        exclude = ('fecha_creacion',)
        
    #con to_representation() especificamos el json que va a devolver y podemos asignarselo manualmente
    # a traves de la instancia    
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'nombre':instance.nombre,
            'descripcion':instance.descripcion,
            'categoria':instance.categoria_id.nombre
        }
        
        
class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        exclude = ('fecha_creacion',)
        
        
class Producto_SucursalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto_Sucursal
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'stock':instance.stock,
            'precio':instance.precio,
            'producto':instance.producto_id.nombre,
            'sucursal':instance.sucursal_id.ciudad
        }
