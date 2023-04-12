from rest_framework import generics

'''
Esta es una clase base para generar las ListApiView de distintos Modelos haciendo herencia
se le asigna un atributo serializer_class que es donde se especificara la clase
y el metodo get_queryset utiliza el serializador y accede a la propiedad meta y a la propiedad model
donde se encuentra el modelo del orm de django para realizar la consulta a la base de datos y retornarla
-> get_serializer() obtiene el serializador que especifico cuando realizo la herencia en views.py
'''
class BaseListApiView(generics.ListAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter()
    
class BaseCreateApiView(generics.CreateAPIView):
    serializer_class = None
    