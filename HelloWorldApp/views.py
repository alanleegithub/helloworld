from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from models import Line

def foo(request,):
    return render_to_response("helloDJ/home.html",
                               {"lines" : Line.objects.all()})


def home(request, name):
    return render_to_response("helloDJ/home.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World " + name + " - Django"})
    #place = models.Place.objects.get(name__iexact=name)
