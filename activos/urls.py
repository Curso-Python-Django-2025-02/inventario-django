from django.urls import path

from activos.views import ActivoDetailView, ActivoListView

app_name = 'activos'
urlpatterns = [
    path('', ActivoListView.as_view(), name='index'),
    path('<int:pk>/', ActivoDetailView.as_view(), name='detail'),
]