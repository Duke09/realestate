from django.contrib import admin

from .models import Realtor

# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    list_per_page = 25