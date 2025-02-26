from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from reparaciones.models import Reparacion

# Create your views here.
class ReparacionListView(ListView):
    model = Reparacion

class ReparacionDetailView(DetailView):
    model = Reparacion

class ReparacionCreateView(CreateView):
    model = Reparacion
    fields = '__all__'

class ReparacionUpdateView(UpdateView):
    model = Reparacion
    fields = '__all__'

class ReparacionDeleteView(DeleteView):
    model = Reparacion
    success_url = reverse_lazy('reparaciones:index')