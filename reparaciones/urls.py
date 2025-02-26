from django.urls import path

from reparaciones.views import ReparacionCreateView, ReparacionDeleteView, ReparacionDetailView, ReparacionListView, ReparacionUpdateView

app_name = 'reparaciones'
urlpatterns = [
    path('', ReparacionListView.as_view(), name='index'),
    path('<int:pk>/', ReparacionDetailView.as_view(), name='detail'),
    path('crear/', ReparacionCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', ReparacionUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ReparacionDeleteView.as_view(), name='eliminar'),
    # TODO: Añadir reparación
    # TODO: Editar reparación
    # TODO: Eliminar reparación
]