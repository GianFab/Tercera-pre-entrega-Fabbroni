from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('curso/', crear_curso_form),
    path('cursos/', mostrar_cursos),
    path('cursoBuscado/', busq_curso_camada),
    path('profe/', crear_profesor_form),
    path('profes/', mostrar_profes),
    path('profeBuscado/', busq_profe_profesion),
    path('estudiante/', crear_estudiante_form),
    path('estudiantes/', mostrar_cursos),
    path('estudianteBuscado/', busq_curso_camada),
    path('entregable/', crear_entregable_form),
    path('entregables/', mostrar_cursos),
    path('entregableBuscado/', busq_curso_camada),
    path('show/', show_html),
]
