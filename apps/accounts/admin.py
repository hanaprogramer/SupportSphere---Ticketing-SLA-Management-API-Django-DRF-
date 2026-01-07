from django.contrib import admin
from .models import *

class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Plan, PlanAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'role', 'plan', 'organization']
    search_fields = ['email']
    list_filter = ['role', 'plan', 'organization']
admin.site.register(CustomUser, CustomUserAdmin)