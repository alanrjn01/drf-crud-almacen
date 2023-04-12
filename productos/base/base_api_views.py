from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


'''
Esta es una clase base para generar el GET y POST de distintos Modelos haciendo herencia
se le asigna un atributo serializer_class que es donde se especificara el serializador
y el metodo get_queryset utiliza el serializador y accede a la propiedad meta y a la propiedad model
donde se encuentra el modelo del orm de django para realizar la consulta a la base de datos y retornarla
-> get_serializer() obtiene el serializador que especifico cuando realizo la herencia en views.py
-> Para poder incluir logica tanto en el get() como en el post() podemos sobreescribir sus metodos
'''

class BaseListCreateApiView(generics.ListCreateAPIView):
    serializer_class = None
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(activo=True)
    
'''
    RetrieveUpdate realiza las funciones de obtener por id, de actualizar un elemento por id y de 
    eliminar un elemento por id hay que definirle el queryset de los productos
    y ya las funciones de get, put y patch y delete de la clase padre se encargan
'''   
class BaseRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = None
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(activo=True)
    
    def delete(self,request,pk=None):
        item = self.get_queryset().filter(id=pk).first()
        if item:
            item.activo = False
            item.save()
            return Response({'message':'deleted'},status=status.HTTP_200_OK)
        return Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)
    