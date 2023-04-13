from rest_framework import generics,response,status
from productos.api.serializers import CategoriaSerializer,ProductoSerializer,SucursalSerializer,Producto_SucursalSerializer
from productos.base.base_api_views import BaseListCreateApiView,BaseRetrieveUpdateDestroyApiView
from productos.base.base_model_view_set import BaseModelViewSet

#ListApiView solamente reconoce la informacion que proviene por el metodo get
#le pasa la consulta al serializador definido e internamente retorna un Response

#Categoria
class CategoriaListApiView(generics.ListAPIView):
    """
    obtiene todas las categorias
    """
    
    #serializador en cual toma la referencia
    serializer_class = CategoriaSerializer
    
    #indicando el queryset (obtiene todos los objetos)
    def get_queryset(self):
        
        categoria = self.get_serializer_class().Meta.model.objects.filter(activo=True)
        return categoria

#clase para crear   
#si decido utilizar logica en la creacion puedo soobrescribir el metodo post(self,request)  
class CategoriaCreateApiView(generics.CreateAPIView):
    """
    recibe un json con los datos de la categoria para crear una insercion
    """
    
    serializer_class = CategoriaSerializer
    
    
    
#clase para obtener (funciona internamente con una primary key)    
class CategoriaRetrieveApiView(generics.RetrieveAPIView):
    """
    recibe una id y la busca en el queryset
    """
    
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        categoria_seleccionada = self.get_serializer_class().Meta.model.objects.filter(activo=True)
        return categoria_seleccionada
    
#clase para eliminar por primary key
#hay que aclarar un get queryset para que el apiview sepa donde buscar 
class CategoriaDestroyApiView(generics.DestroyAPIView):
    """
    realiza una eliminacion a nivel logico y no de base de datos, ya que no elimina la instancia de la base
    sino que cambia su atributo 'activo' a False y de esta forma el elemento ya no se obtiene en las peticiones
    """
    
    serializer_class = CategoriaSerializer
    
    
    def get_queryset(self):
        categorias = self.get_serializer().Meta.model.objects.filter(activo = True)
        return categorias
    
    #eliminacion logica:
    #filtro en el queryset de categorias buscando la primary key 
    #paso el estado de activo a falso, lo guardo y despues retorno una response
    def delete(self,request,pk=None):
        categoria_seleccionada = self.get_queryset().filter(id=pk).first()
        print(categoria_seleccionada)
        if categoria_seleccionada:
            categoria_seleccionada.activo = False
            categoria_seleccionada.save()
            return response.Response({'message':'deleted'},status=status.HTTP_200_OK)
        return response.Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)
    
#clase para actualizar
class CategoriaUpdateApiView(generics.UpdateAPIView):
    """
    recibe una primary key y busca el elemento en el queryset, si encuentra el elemento lo serializa 
    con la data recibida en el request, si pasa las validaciones el serializer se guarda
    """
    
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        categorias = self.get_serializer().Meta.model.objects.filter(activo = True)
        return categorias
    
    
    #obtengo la instancia de la categoria a actualizar 
    #si es distinta a None, utilizo el serializer de la clase y le paso la instancia y la data de request
    #compruebo las validaciones del serializer
    #luego guardo en la base de datos el serializador y hago un response
    def put(self,request,pk=None):
        categoria_a_actualizar = self.get_queryset().filter(id=pk).first()
        if categoria_a_actualizar:
            serializer_a_actualizar = self.serializer_class(categoria_a_actualizar,data = request.data)
            if serializer_a_actualizar.is_valid():
                serializer_a_actualizar.save()
                return response.Response(serializer_a_actualizar.data,status=status.HTTP_200_OK)
            return response.Response(serializer_a_actualizar.errors,status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'message':'not found'},status=status.HTTP_404_NOT_FOUND)
            
        
    
#utilizando jerarquia de clases:    
#-----------
#Producto    

class ProductoListCreateApiView(BaseListCreateApiView):
    serializer_class = ProductoSerializer
    
class ProductoRetrieveUpdateDestroyApiView(BaseRetrieveUpdateDestroyApiView):
    serializer_class = ProductoSerializer
#-----
#Sucursal
    
class SucursalModelViewSet(BaseModelViewSet):
    serializer_class = SucursalSerializer
        
    
#--------   
#Producto_Sucursal    
class ProductoSucursalModelViewSet(BaseModelViewSet):
    serializer_class = Producto_SucursalSerializer

    


