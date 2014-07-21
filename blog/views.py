from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

# Create your views here.

def hello(request):
   name = "Bogo"
   html = "<html><body>Hi %s from views.py. </body></html>" %name
   return HttpResponse(html)

def hello_template(request):
   name = "Bogo"
   tp = get_template("hello.html")
   html = tp.render(Context({'name': name}))
   return HttpResponse(html)

def hello_template_simple(request):
   name = 'Bogo'
   return return_to_render('hello.html', {'name': name})

class HelloTemplate(TemplateView):
   template_name = "hello_class.html"

   def get_context_data(self, **kwargs):
      context = super(HelloTemplate, self).get_context_data(**kwargs)
      context['name'] = 'Bogo'
      return context
