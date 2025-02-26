from django.db import models
from django.urls import reverse

# Create your models here.
class Reparacion(models.Model):
    activo = models.ForeignKey('activos.Activo', on_delete=models.CASCADE)
    fecha = models.DateField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return f"#{self.pk} - {self.activo}"
    
    def get_absolute_url(self):
        return reverse('reparaciones:detail', kwargs={'pk': self.pk})