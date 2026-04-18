from django.contrib import admin
from myapp.models import *
# Register your models here.

class empdisplay(admin.ModelAdmin):
    list_display=['id',"name","email","phone","deparment","image"]
admin.site.register(Emp)
