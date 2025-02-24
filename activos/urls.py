from django.urls import path

from activos.views import ActivoDetailView, ActivoListView, ActivoCreateView, ActivoUpdateView, ActivoDeleteView

app_name = 'activos'
urlpatterns = [
    path('', ActivoListView.as_view(), name='index'),
    path('<int:pk>/', ActivoDetailView.as_view(), name='detail'),
    path('crear/', ActivoCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', ActivoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ActivoDeleteView.as_view(), name='eliminar'),
]