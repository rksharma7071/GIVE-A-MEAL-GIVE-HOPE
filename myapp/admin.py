from django.contrib import admin
from .models import *


@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donator_name', 'food_type', 'quantity', 'expiry_date', 'pickup_time', 'pickup_location', 'action')
    
