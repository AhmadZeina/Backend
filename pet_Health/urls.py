from django.urls import path

from . import views

app_name = 'pet_Health'

urlpatterns  = [

    # /pet_Health/
    path('', views.index , name='index') , 


    # /pet_Health/1234
    path('<int:disease_id>/' , views.detail , name = 'detail') , 


    # /pet_Health/1234
    #path(r"^(?P<disease_id>[0-9]+)/$", views.detail , name='detail') , 
         



]