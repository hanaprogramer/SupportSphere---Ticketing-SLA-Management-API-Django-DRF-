from django.db import models
from apps.accounts.models import Plan

class SLAPolicy(models.Model):
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name="sla_policy")
    low_hours = models.PositiveIntegerField()
    medium_hours = models.PositiveIntegerField()
    high_hours = models.PositiveIntegerField()
    urgent_hours = models.PositiveIntegerField()

    def __str__(self):
        return f"SLA Policy for {self.plan.name}"