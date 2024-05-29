from django.contrib import admin
from django.db import models
from .models import Disease
from django.contrib.admin.widgets import AdminTextareaWidget

# Register your models here.

class DiseasAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': AdminTextareaWidget},
    }
    
    list_display = ('disease_name', 'animal', 'short_common_signs', 'hurt_degree', 'short_treatment' )

    def short_common_signs(self, obj):
        return obj.common_signs[:50]

    def short_treatment(self, obj):
        return obj.treatment[:50]


    
admin.site.register(Disease , DiseasAdmin) 