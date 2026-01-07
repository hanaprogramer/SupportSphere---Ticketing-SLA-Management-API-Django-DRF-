from django.contrib import admin
from .models import *

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['actor', 'action_type', 'object_type', 'object_id', 'created_at']
    list_filter = ['action_type', 'object_type']
    search_fields = ['actor__email']