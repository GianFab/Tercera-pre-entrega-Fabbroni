from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('curso/', crear_curso_form),
    path('profe/', crear_profesor_form),
    path('estudiante/', crear_estudiante_form),
    path('entregable/', crear_entregable_form),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
    path('cursoBuscado/', busq_curso_camada)

]
