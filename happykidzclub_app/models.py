from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
from django.db import models

class Appointment(models.Model):
    guardian_name = models.CharField(max_length=100)
    guardian_email = models.EmailField()
    child_name = models.CharField(max_length=100)
    child_age = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    guardian_name = models.CharField(max_length=100)
    guardian_email = models.EmailField()
    child_name = models.CharField(max_length=100)
    child_age = models.CharField(max_length=10)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"{self.guardian_name} - {self.child_name} ({self.created_at.strftime('%Y-%m-%d')})"

    class Meta:
        ordering = ['-created_at']