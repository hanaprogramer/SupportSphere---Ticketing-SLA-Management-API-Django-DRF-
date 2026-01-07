from django.db import models
from apps.organizations.models import *
from apps.accounts.models import *
class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ("LOW","low"),
        ("MEDIUM","medium"),
        ("HIGH","high"),
        ("URGENT","urgent")
        ]
    
    STATUS_CHOICES = [
        ("OPEN","open"),
        ("IN_PROGRESS","in_progress"),
        ("WAITING","waiting"),
        ("CLOSED","closed")
    ]

    CATEGORY_CHOICES = [
        ("PAYMENT","payment"),
        ("BUG","bug"),
        ("ACCOUNT","account"),
        ("OTHER","other"),
    ]
    title = models.CharField(max_length=60)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="tickets")
    created_by = models.ForeignKey(
    CustomUser,
    on_delete=models.CASCADE,
    related_name="created_tickets",
    limit_choices_to={"role": "CUSTOMER"}
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    assigned_agent = models.ForeignKey(
    CustomUser,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name="assigned_tickets",
    limit_choices_to={"role": "AGENT"}
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="OTHER")
    sla_deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_response_at = models.DateTimeField(null=True, blank=True)
    is_sla_violated = models.BooleanField(default=False)

#===================================================
class TicketReply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="replies")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="replies")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
#===================================================
class PlanUpgradeRequest(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("NOT_REQUIRED", "not_required"),
        ("PENDING", "pending"),
        ("VERIFIED", "verified"),
        ("FAILED", "failed"),
    ]

    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="plan_upgrade_requests",
        limit_choices_to={"role": "CUSTOMER"},
    )

    current_plan = models.ForeignKey(
        Plan,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="current_plan_requests",
    )

    requested_plan = models.ForeignKey(
        Plan,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="requested_plan_requests",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="PENDING",
    )

    note = models.TextField(null=True, blank=True)

    reviewed_by = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviewed_plan_requests",
        limit_choices_to={"role": "ADMIN"},
    )

    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.email} -> {self.requested_plan} ({self.status})"