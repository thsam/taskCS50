from django.urls import path
from . import views
app_name = "tasks" #importante para evitar la colision
urlpatterns = [ 
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]