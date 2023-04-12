from django.contrib import admin
from .models import Categoria,Producto,Sucursal,Producto_Sucursal

#añadiendo al panel de administrador una columna con las ID de categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Producto_Sucursal)
