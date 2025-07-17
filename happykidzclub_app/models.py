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