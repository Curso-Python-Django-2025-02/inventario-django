from django.contrib import admin

from activos.models import Activo, Etiqueta, Ubicacion

# Register your models here.
admin.site.register(Activo)
admin.site.register(Etiqueta)
admin.site.register(Ubicacion)