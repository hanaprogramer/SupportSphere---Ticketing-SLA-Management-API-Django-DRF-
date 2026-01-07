from apps.organizations.models import *
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Plan(models.Model):
    NAME_CHOICES = [
        ("FREE","free"),
        ("PRO","pro"),
        ("ENTERPRISE","enterprise")
    ]
    name = models.CharField(max_length=15, choices=NAME_CHOICES, default='free')
    description = models.TextField()
    def __str__(self):
        return self.name
#=================================================================================================
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
#=================================================================================================
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("ADMIN","admin"),
        ("AGENT","agent"),
        ("CUSTOMER","customer"),
        ("MANAGER","manager")
        ]
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, related_name='users', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

