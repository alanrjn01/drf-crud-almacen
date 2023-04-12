from rest_framework.routers import DefaultRouter #importando el router
from productos.api.views import SucursalModelViewSet,ProductoSucursalModelViewSet
from django.urls import include

#inicializando el router
router = DefaultRouter()

#registrando la ruta de sucursal y su vista
router.register(r'sucursal',SucursalModelViewSet,basename='sucursal')
router.register(r'producto_sucursal',ProductoSucursalModelViewSet,basename='producto_sucursal')

#agregando la lista de urls de router al urlpatterns para despues llamarlo en urls.py del proyecto
urlpatterns = router.urls