from django.db import models

from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    salt = models.CharField(max_length=64)
    password_hash = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} - {self.status}"

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action}"
