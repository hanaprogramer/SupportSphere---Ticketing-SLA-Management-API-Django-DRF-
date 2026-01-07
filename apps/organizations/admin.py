from django.contrib import admin
from .models import *

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

admin.site.register(Organization, OrganizationAdmin)    