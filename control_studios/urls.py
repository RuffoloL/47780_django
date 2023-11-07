from django.urls import path

from control_studios.views import listar_estudiantes

#Estas son las URLS de la app control_studios
urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
]