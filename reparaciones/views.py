from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from activos.models import Activo
from reparaciones.forms import ReparacionFilterForm
from reparaciones.models import Reparacion
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ReparacionListView(ListView):
    model = Reparacion

    def get_queryset(self):
        qs = super().get_queryset()
        form = ReparacionFilterForm(self.request.GET)
        if form.is_valid():
            if 'activo' in form.cleaned_data and form.cleaned_data['activo']:
                qs = qs.filter(activo=form.cleaned_data['activo'])
            if 'fecha_desde' in form.cleaned_data and form.cleaned_data['fecha_desde']:
                qs = qs.filter(fecha__gte=form.cleaned_data['fecha_desde'])
            if 'fecha_hasta' in form.cleaned_data and form.cleaned_data['fecha_hasta']:
                qs = qs.filter(fecha__lte=form.cleaned_data['fecha_hasta'])
        return qs
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['form'] = ReparacionFilterForm(initial=self.request.GET)
        return contexto


class ReparacionDetailView(DetailView):
    model = Reparacion

class ReparacionCreateView(LoginRequiredMixin, CreateView):
    model = Reparacion
    fields = '__all__'

class ReparacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Reparacion
    fields = '__all__'

class ReparacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Reparacion
    success_url = reverse_lazy('reparaciones:index')


# Listado de reparaciones de un determinado activo
class ReparacionesActivoListView(ListView):
    model = Reparacion
    template_name = 'reparaciones/reparaciones_activo_list.html'

    def setup(self, request, *args, **kwargs):
        self.activo_id = kwargs['activo_id']
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(activo=self.activo_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activo'] = Activo.objects.get(pk=self.activo_id)
        return context