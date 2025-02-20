from django.urls import path

from activos.views import ActivoDetailView, ActivoListView

urlpatterns = [
    path('', ActivoListView.as_view(), name='activos:index'),
    path('<int:pk>/', ActivoDetailView.as_view(), name='activos:detail'),
]