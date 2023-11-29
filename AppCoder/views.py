from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# def saludo_plantilla(request):
#     contexto = {
#         "nombre": "Gian",
#         "edad": 23,
#         "perros": [
#             {
#                 "nombre": "Berta",
#                 "edad": 6,
#             },
#             {
#                 "nombre": "Lola",
#                 "edad": 5,
#             },
#             {
#                 "nombre": "Blass",
#                 "edad": 11,
#             },
#             {
#                 "nombre": "Cleto",
#                 "edad": 7,
#             },
#         ],
#     }
#     return render(request, "index.html", contexto)


def crear_curso(request):
    curso = Curso(nombre="Python", camada=7895)
    curso.save()
    contexto = {
        "curso": curso
    }

    return render(request, "index.html", contexto)

def show_html(request):

    contexto = {
        "nombre": "Gian",
    }
    return render(request, "index.html", contexto)


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos
    }
    return render(request, "AppCoder/cursos.html", contexto)

