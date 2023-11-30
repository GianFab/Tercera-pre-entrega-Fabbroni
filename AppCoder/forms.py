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

class BusqEstudianteForm(forms.Form):
    apellido = forms.CharField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class BusqProfeForm(forms.Form):
    profesion = forms.CharField()

class EntregableForm(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()

class BusqEntregableForm(forms.Form):
    nombre = forms.CharField()