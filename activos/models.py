from django.db import models
from django.urls import reverse

# Create your models here.
class Activo(models.Model):

    class Estados(models.TextChoices):
        ACTIVO = 'A', 'Activo'
        BAJA = 'B', 'Baja'
        REPARACION = 'R', 'Reparación'

    nombre = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=50, unique=True, 
                                 verbose_name='Número de serie')
    fecha_adquisicion = models.DateField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    vida_util = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=1,
                              choices=Estados, default=Estados.ACTIVO)
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.PROTECT)
    etiquetas = models.ManyToManyField('Etiqueta')
    foto = models.ImageField(upload_to='activos_fotos', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.num_serie})"
    
    def get_absolute_url(self):
        return reverse('activos:detail', kwargs={'pk': self.pk})


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    lugar = models.CharField(max_length=100)

    def __str__(self):
        return self.lugar