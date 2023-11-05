from django.shortcuts import render

def listar_estudiantes(request):
    contexto = {
        "profesor": "Pedro",
        "estudiantes": [
            {"nombre": "Erik", "apellido": "Harmitton", "nota": 9},
            {"nombre": "Nicolas", "apellido": "Lanvers", "nota": 8},
            {"nombre": "Sebastian", "apellido": "Antonini", "nota": 10},
            {"nombre": "Mariano", "apellido": "Martina", "nota": 7},  
        ]
    }
    http_response = render(
        request=request,
        template_name='control_studios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response