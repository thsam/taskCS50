from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django import forms #formularios
from django.urls import reverse
from django.http import HttpResponseRedirect
#tasks = ["foo", "bar", "baz"]
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #proprity=forms.IntegerField(label=" Priority", min_value=1,max_value=10) #prioridad



# Create your views here. 
def index(request): # la vista atiende mi requerim renderizando el html y le pasa el argumento tasks
    #trabajando con sesiones
    if "tasks" not in request.session:
        request.session["tasks"] = []
    # fin trabajando con sesiones
    return render(request, "tasks/index.html", {
        #"tasks": tasks
        "tasks": request.session["tasks"]
    })
# Add a new task: 

""" def add(request):
    return render(request, "tasks/add.html") """
#usamos formularios de django

def add(request): 
    #validaciones por el servidor
    if request.method =="POST":
        form = NewTaskForm(request.POST) #declaramos una variable y traemos el requerimiento POST
        if form.is_valid():
            task=form.cleaned_data["task"] #Me da acceso a todos los datos que el usuario envió,
                                            # si quiero saber q tarea enviaron ["task"]
            #tasks.append(task) #agrego la tarea a mi lista de tareas
            #por la sesiones ahora cambio a:
            request.session["tasks"] += [task] #almacenando en una sesion
            return HttpResponseRedirect(reverse("tasks:index")) #entonces, redirige a la pagina de tareas, sin codificar la url --> que el mismo
                                                                #busque el url que esta en la aplicación y name index
        else:
            #si no es válido, debo volver al archivo add.html nuevamente con la info
            #para que vean loserroes que cometieron y hagan modificaciones
            return render(request,"tasks/add.html",{
              # If the form is invalid, re-render the page with existing information.             return render(request, "tasks/add.html", {
                "form": form
            })
    else: # si el método no fue post
        return render(request, "tasks/add.html", {
            "form": NewTaskForm() #le damos el formulario vacío
        })


