from django.urls import include, path

from activos.views import ActivoDetailView, ActivoListView, ActivoCreateView, ActivoUpdateView, ActivoDeleteView, ActivoViewSet, UbicacionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'activos', ActivoViewSet)
router.register(r'ubicaciones', UbicacionViewSet)

app_name = 'activos'
urlpatterns = [
    path('', ActivoListView.as_view(), name='index'),
    path('<int:pk>/', ActivoDetailView.as_view(), name='detail'),
    path('crear/', ActivoCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', ActivoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ActivoDeleteView.as_view(), name='eliminar'),
    path('api/', include(router.urls))
]