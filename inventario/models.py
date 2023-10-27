from django.db import models

class Categorias(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
    
    class Meta:
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
class Productos(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos_imagenes/', null=True, blank=True)

    
    ORIGEN_CHOICES = [
        ('NAC', 'NACIONAL'),
        ('IMP', 'IMPORTADO'),
    ]
    origen = models.CharField(max_length=3, choices=ORIGEN_CHOICES, default='NAC')
    
    categoria_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
