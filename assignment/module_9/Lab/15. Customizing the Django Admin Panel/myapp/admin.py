from django.contrib import admin
from myapp.models import *
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'specialty',
        'experience',
        'available'
    )

    search_fields = (
        'name',
        'specialty'
    )

admin.site.register(Doctor,DoctorAdmin)
