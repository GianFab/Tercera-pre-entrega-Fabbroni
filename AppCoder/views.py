from django.http import HttpResponse
from django.shortcuts import *
from AppCoder.models import *
from AppCoder.forms import *


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "form": BusqCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", contexto)


def crear_curso_form(request):

    if request.method == "POST":
        curso_formulario = CursoForm(request.POST)
        if curso_formulario.is_valid():
            info = curso_formulario.cleaned_data
            curso_crear = Curso(nombre=info["nombre"], camada=info["camada"])
            curso_crear.save()
            return redirect("/app/cursos/")

    curso_formulario = CursoForm()
    contexto = {
        "form": curso_formulario
    }
    return render(request, "AppCoder/crear_curso.html", contexto)


def busq_curso_camada(request):
    camada = request.GET["camada"]
    cursos = Curso.objects.filter(camada__icontains=camada)
    contexto = {
        "cursos": cursos,
        "form": BusqCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", contexto)


def mostrar_profes(request):
    profes = Profesor.objects.all()
    contexto = {
        "profes": profes,
        "form": BusqProfeForm(),
    }
    return render(request, "AppCoder/profes.html", contexto)

def crear_profesor_form(request):

    if request.method == "POST":
        profe_formulario = ProfesorForm(request.POST)
        if profe_formulario.is_valid():
            info = profe_formulario.cleaned_data
            profe_crear = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
            profe_crear.save()
            return redirect("/app/profes/")


    profe_formulario = ProfesorForm()
    contexto = {
        "form": profe_formulario
    }
    return render(request, "AppCoder/crear_profesor.html", contexto)

def busq_profe_profesion(request):
    profesion = request.GET["profesion"]
    profes = Profesor.objects.filter(profesion__icontains=profesion)
    contexto = {
        "profes": profes,
        "form": BusqProfeForm(),
    }
    return render(request, "AppCoder/profes.html", contexto)

def crear_estudiante_form(request):
    estudiante_formulario = EstudianteForm()
    contexto = {
        "form": estudiante_formulario
    }
    return render(request, "AppCoder/crear_curso.html", contexto)

def crear_entregable_form(request):
    entregable_formulario = EntregableForm()
    contexto = {
        "form": entregable_formulario
    }
    return render(request, "AppCoder/crear_curso.html", contexto)




def show_html(request):

    contexto = {
        "nombre": "Gian",
    }
    return render(request, "index.html", contexto)
