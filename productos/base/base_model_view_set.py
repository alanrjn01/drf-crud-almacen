from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# https://www.django-rest-framework.org/api-guide/viewsets/

#ModelViewSet 
'''
    Se encarga de manejar los metodos http del crud. tambien se puede sobreescribir los metodos
    tambien gestiona las url a partir de un router (routers.py)
'''

class BaseModelViewSet(ModelViewSet):
    serializer_class = None
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(activo=True)
    
    def destroy(self,request,pk=None):
        item = self.get_queryset().filter(id=pk).first()
        if item:
            item.activo = False
            item.save()
            return Response({'message':'deleted'},status=status.HTTP_200_OK)
        return Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)