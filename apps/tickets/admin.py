from django.contrib import admin
from .models import Ticket, TicketReply, PlanUpgradeRequest

class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'created_by', 'status', 'priority']
admin.site.register(Ticket, TicketAdmin)

class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'sender', 'created_at']
admin.site.register(TicketReply, TicketReplyAdmin)

class PlanUpgradeRequestAdmin(admin.ModelAdmin):
    list_display = ['customer', 'current_plan', 'requested_plan', 'status', 'payment_status', 'created_at']
    list_filter = ['status', 'payment_status']
admin.site.register(PlanUpgradeRequest, PlanUpgradeRequestAdmin)
