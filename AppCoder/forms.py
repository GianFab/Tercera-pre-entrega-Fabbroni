from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class BusqCursoForm(forms.Form):
    camada = forms.IntegerField()

class EstudianteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class BusqProfeForm(forms.Form):
    profesion = forms.CharField()

class EntregableForm(forms.Form):
    nombre = forms.CharField()
    entregado = forms.BooleanField()