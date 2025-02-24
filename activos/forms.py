from django import forms

from activos.models import Activo



class ActivoFilterForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput({'class': 'form-control'}))  # Texto que ha de contener el nombre
    num_serie = forms.CharField(max_length=50, required=False)  # Texto que ha de coincidir exactamente con el número de serie
    estado = forms.ChoiceField(
        choices=[('', '---'), *Activo.Estados.choices], 
        required=False)
    fecha_adquisicion_desde = forms.DateField(
        required=False,
        widget=forms.DateInput({'type': 'date', 'class': 'form-control'})) # Input de tipo fecha en el HTML
    fecha_adquisicion_hasta = forms.DateField(
        required=False,
        widget=forms.DateInput({'type': 'date'}))
        