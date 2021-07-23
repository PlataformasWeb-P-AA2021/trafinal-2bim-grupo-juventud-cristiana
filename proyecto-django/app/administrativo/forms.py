from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import *

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese apellido por favor'),
            'cedula': _('Ingrese cédula por favor'),
            'correo': _('Ingrese correo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        valor = "René"
        ["René"] # 1
        len( ["René"])
        """

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_correo(self):
        valor = self.cleaned_data['correo']
        if "@" not in valor or "utpl.edu.ec" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad")
        return valor


class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']

class CasasForm(ModelForm):
    class Meta:
        model = Casas
        fields = ['barrio', 'direccion', 'propietario', 'valor', 'color', 'cuartos', 'pisos']

class DepartamentosForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = ['barrio', 'direccion', 'propietario', 'valor',  'cuartos', 'mensual']