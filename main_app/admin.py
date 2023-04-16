from django.contrib import admin
# Register your models here.
from .models import *
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'title']