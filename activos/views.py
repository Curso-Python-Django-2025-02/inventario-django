from django.shortcuts import render
from django.views.generic import ListView, DetailView

from activos.models import Activo

# Create your views here.
class ActivoListView(ListView):
    model = Activo


class ActivoDetailView(DetailView):
    model = Activo
    