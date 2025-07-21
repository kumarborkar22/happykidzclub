from rest_framework import serializers
from .models import ContactMessage

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        

from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'guardian_name', 'guardian_email', 'child_name', 'child_age', 'message', 'created_at', 'status']
        read_only_fields = ['id', 'created_at']

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['guardian_name', 'guardian_email', 'child_name', 'child_age', 'message']