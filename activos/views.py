from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from activos.forms import ActivoFilterForm
from activos.models import Activo, Ubicacion
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from rest_framework import viewsets

from activos.serializers import ActivoSerializer, UbicacionSerializer
from rest_framework import permissions

# Create your views here.
class ActivoListView(ListView):
    template_name = 'activos/activo_list.html'
    model = Activo

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['form'] = ActivoFilterForm(initial=self.request.GET)
        return contexto
    
    def get_queryset(self):
        qs = super().get_queryset()
        form = ActivoFilterForm(self.request.GET)
        if form.is_valid():
            if 'nombre' in form.cleaned_data and form.cleaned_data['nombre']: # Si está presente y no es vacío
                qs = qs.filter(nombre__icontains=form.cleaned_data['nombre'])
            if 'num_serie' in form.cleaned_data and form.cleaned_data['num_serie']:
                qs = qs.filter(num_serie=form.cleaned_data['num_serie'])
            if 'estado' in form.cleaned_data and form.cleaned_data['estado']:
                qs = qs.filter(estado=form.cleaned_data['estado'])
            if 'fecha_adquisicion_desde' in form.cleaned_data and form.cleaned_data['fecha_adquisicion_desde']:
                qs = qs.filter(fecha_adquisicion__gte=form.cleaned_data['fecha_adquisicion_desde'])
            if 'fecha_adquisicion_hasta' in form.cleaned_data and form.cleaned_data['fecha_adquisicion_hasta']:
                qs = qs.filter(fecha_adquisicion__lte=form.cleaned_data['fecha_adquisicion_hasta'])
        return qs


class ActivoDetailView(DetailView):
    model = Activo
    
class ActivoCreateView(LoginRequiredMixin, CreateView):
    model = Activo
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.has_perm('activos.add_activo'):
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('No tienes permiso para crear activos')

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.has_perm('activos.add_activo'):
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('No tienes permiso para crear activos')



class ActivoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Activo
    fields = '__all__'
    permission_required = 'activos.change_activo'

class ActivoDeleteView(LoginRequiredMixin, DeleteView):
    model = Activo
    success_url = reverse_lazy('activos:index')


# Vistas de API REST
class ActivoViewSet(viewsets.ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [permissions.IsAuthenticated]