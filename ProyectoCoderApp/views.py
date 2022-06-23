import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Curso, Estudiante

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    # nombre = "Python"
    # comision = 31080

    # nuevo_curso = Curso(nombre=nombre,comision=comision)
    # nuevo_curso.save()

    cursos = Curso()

    lista_cursos = [x.nombre for x in Curso.objects.all()] # para obtener los nombres de los cursos y listarlos

    return HttpResponse(f"Cursos: {str(lista_cursos)}")

def profesores(request):
    return render(request,"ProyectoCoderApp/profesores.html",{})

def estudiantes(request):
    estudiantes= Estudiante.objects.all()

    return render(request,"ProyectoCoderApp/estudiantes.html",{"estudiantes":estudiantes})

def crear_curso(request):
    # return HttpResponse("Vista de cursos")
    #POST    
    if request.method == "POST":

        info_formulario= request.POST
        
        curso= Curso(nombre = info_formulario["nombre"],comision = int(info_formulario["comision"]))

        curso.save()

        return redirect("inicio")
        
    #GET y otros
    else:
        return render(request,"ProyectoCoderApp/formulario_curso.html",{})
    

def cursos(request):
    # return HttpResponse("Vista de cursos")

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")