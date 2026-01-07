from django.db import models
from apps.accounts.models import *
class AuditLog(models.Model):
    ACTION_TYPE_CHOICES = [
        ("CREATE","create"),
        ("UPDATE","update"),
        ("DELETE","delete")
        ]
    
    OBJECT_TYPE = [
        ("TICKET","ticket"),
        ("REPLY","reply"),
        ("PLANREQUEST","planrequest"),
        ("ETC","etc")
        ]
    
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="audit_logs")
    action_type = models.CharField(max_length=10, choices=ACTION_TYPE_CHOICES)
    object_type = models.CharField(max_length=15, choices=OBJECT_TYPE)
    object_id = models.PositiveIntegerField()   # The ID is something that has changed
    before_data = models.JSONField(null=True, blank=True)
    # What was the situation before the change?
    # for example : {"status": "closed", "priority": "high"}
    after_data = models.JSONField(null=True, blank=True)
    # What was the situation after the change?
    # for example : {"status": "closed", "priority": "high"}
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actor.email} {self.action_type} {self.object_type}({self.object_id})"

