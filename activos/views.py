from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from activos.forms import ActivoFilterForm
from activos.models import Activo

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
    
class ActivoCreateView(CreateView):
    model = Activo
    fields = '__all__'

class ActivoUpdateView(UpdateView):
    model = Activo
    fields = '__all__'

class ActivoDeleteView(DeleteView):
    model = Activo
    success_url = reverse_lazy('activos:index')
