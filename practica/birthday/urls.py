from django.urls import path

from . import views
#2 AGREGO LA URL
urlpatterns = [
    path("", views.index, name="index")
]