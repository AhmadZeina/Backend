from django.db import models

class Disease (models.Model) :
    disease_name = models.CharField(max_length=150)
    
    on_pet = (
        ('cat','Cat') ,
        ('dog','Dog') ,
    )

    animal = models.CharField(max_length=3, choices=on_pet)
    common_signs = models.TextField(default="this is the most common signs")

    disease_degree = (
        ('mild','Mild') ,
        ('moderate','Moderate') ,
        ('moderately_severe','Moderately_severe') ,
        ('severe','Severe') ,
        ('critical','Critical') ,

    )
    
    hurt_degree = models.CharField(max_length=50 , choices=disease_degree)



    treatment = models.TextField(default="These are the treatments we recommend")

