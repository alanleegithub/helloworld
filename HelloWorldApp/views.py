from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
def foo(request,):
    return render_to_response("helloDJ/home.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})
