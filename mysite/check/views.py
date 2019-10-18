from django.http import HttpResponse
from .models import Program
from django.template import loader

#def index(request):
#    return HttpResponse("Hello World");
# Create your views here.

def select(request,id):
    q = Program.objects.get(id=1);
    return HttpResponse();

def index(request):
   program_list = Program.objects.order_by('id')
   template = loader.get_template('check/index.html')
   context = {
       'program_list':program_list
   }
   return HttpResponse(template.render(context,request))
    