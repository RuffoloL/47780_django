from django.shortcuts import render

from control_studios.models import Estudiante

def listar_estudiantes(request):
    contexto = {
        "profesor": "Pedro",
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_studios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response