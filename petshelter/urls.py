from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('' , include("homepage.urls")) ,
    path('admin/', admin.site.urls),
    path("__debug__/", include('debug_toolbar.urls')),
    path('playground/' , include ('playground.urls') ),
    path("polls/", include("polls.urls")),
    path('pet_Health/' , include("pet_Health.urls")) ,
]
