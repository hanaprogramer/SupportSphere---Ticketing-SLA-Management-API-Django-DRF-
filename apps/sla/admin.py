from django.contrib import admin
from .models import *

class SLAPolicyAdmin(admin. ModelAdmin):
    list_display = ['plan', 'low_hours', 'medium_hours', 'high_hours', 'urgent_hours']
    list_filter = ['plan']
    
admin.site.register(SLAPolicy, SLAPolicyAdmin)    