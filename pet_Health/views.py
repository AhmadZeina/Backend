from django.shortcuts import render
from django.http import HttpResponse
from .models import Disease
from django.shortcuts import get_object_or_404

# Create your views here.

#def index (request) :
 #    all_diseases = Disease.objects.all()
  #   html = '' 
   #  for disease in all_diseases :
    #      
     #     url='/pet_Health/' + str(disease.id) + '/'
      #    html += '<a href = " ' + url + ' ">' + disease.disease_name + '</a><br>'

     #return HttpResponse (html)


def index(request) :
     all_diseases = Disease.objects.all()
     context = {
          "all_diseases" : all_diseases ,
     }
     return render (request , 'pet_Health/index.html' , context)
     

def detail(request , disease_id ) :
    # selected_disease = get_object_or_404(Disease, pk=disease_id)
    selected_disease = Disease.objects.get(pk=disease_id)
    context = {
          'selected_disease' : selected_disease
     }
    return render (request , "pet_Health/detail.html" , context)