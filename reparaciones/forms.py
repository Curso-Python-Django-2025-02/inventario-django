from django import forms

from activos.models import Activo

class ReparacionFilterForm(forms.Form):
    activo = forms.ModelChoiceField(
        queryset=Activo.objects.all(),
        required=False,
        widget=forms.Select({'class': 'form-control'}))
    fecha_desde = forms.DateField(
        required=False,
        widget=forms.DateInput({'type': 'date', 'class': 'form-control'}))
    fecha_hasta = forms.DateField(
        required=False,
        widget=forms.DateInput({'type': 'date', 'class': 'form-control'}))
