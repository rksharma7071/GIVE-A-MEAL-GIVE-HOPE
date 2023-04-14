from django.contrib import admin
from .models import *


@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    
