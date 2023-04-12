from django.db import models

#implicitamente si no se especifica los campos no pueden ser nulos

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=300,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    
class Sucursal(models.Model):
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=300)
    fecha_creacion = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    #la clase meta define los metadatos de la clase
    class Meta:
        verbose_name='Sucursal'
        verbose_name_plural='Sucursales'
    
    def __str__(self):
        return f'{self.nombre} - {self.direccion}'
    
class Producto_Sucursal(models.Model):
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    sucursal_id = models.ForeignKey(Sucursal,on_delete=models.CASCADE)
    stock = models.IntegerField()
    precio = models.FloatField()
    
    class Meta:
        verbose_name='Producto_Sucursal'
        verbose_name_plural='Producto_Sucursales'
        
    def __str__(self):
        return f'{self.producto_id} --- Stock: {self.stock} - Precio: {self.precio}'
    
    
    
    