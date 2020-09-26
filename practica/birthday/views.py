import datetime

from django.shortcuts import render

# Create your views here.


# Create your views here. 1) AGREGO UNA VISTA
from django.shortcuts import render
def index(request):
    now = datetime.datetime.now()
    return render(request, "birthday/index.html", {
        "birthay": now.month == 9 and now.day == 27
    })