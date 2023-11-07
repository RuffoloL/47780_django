from django.shortcuts import render, redirect
from django.urls import reverse

from control_studios.models import Estudiante, Curso

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

def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_studios/lista_cursos.html',
        context=contexto,
    )
    return http_response


def crear_curso(request):
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='control_studios/formulario_curso_a_mano.html',
    )
    return http_response
    
        
    
