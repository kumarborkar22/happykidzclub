from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def classes(request):
    # Handle appointment form submission - SAME PATTERN AS CONTACT
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save appointment to database
            Appointment.objects.create(**form.cleaned_data)
            messages.success(request, "Your appointment has been submitted successfully!")
            return redirect('classes')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AppointmentForm()
    
    return render(request, 'classes.html', {'form': form})

from django.core.mail import send_mail
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            send_mail(
                subject=form.cleaned_data['subject'],
                message=f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}",
                from_email=form.cleaned_data['email'],
                recipient_list=['kumarborkar403@gmail.com'],
            )
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def facility(request):
    return render(request, 'facility.html')

def team(request):
    return render(request, 'team.html')

def call_to_action(request):
    return render(request, 'call-to-action.html')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, 'Your appointment has been successfully submitted! We will contact you soon.')
            return redirect('appointment')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})

def testimonial(request):
    return render(request, 'testimonial.html')

def error_404(request, exception):
    return render(request, '404.html', status=404)

def gallery(request):
    images = range(1, 31)  # 1 to 30
    return render(request, 'gallery.html', {'images': images})

# api views....

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactMessageSerializer

@api_view(['GET'])
def contact_messages_api(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    serializer = ContactMessageSerializer(messages, many=True)
    return Response(serializer.data)




from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .forms import AppointmentForm
from .serializers import AppointmentSerializer, AppointmentCreateSerializer
import json
# API Views for Postman testing
@api_view(['GET', 'POST'])
def appointment_api(request):
    """
    GET: List all appointments
    POST: Create new appointment
    """
    if request.method == 'GET':
        appointments = Appointment.objects.all().order_by('-created_at')
        serializer = AppointmentSerializer(appointments, many=True)
        return Response({
            'success': True,
            'count': len(serializer.data),
            'appointments': serializer.data
        })
    
    elif request.method == 'POST':
        serializer = AppointmentCreateSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()
            response_serializer = AppointmentSerializer(appointment)
            return Response({
                'success': True,
                'message': 'Appointment created successfully!',
                'appointment': response_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail_api(request, pk):
    """
    GET: Get specific appointment
    PUT: Update appointment
    DELETE: Delete appointment
    """
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Appointment not found'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response({
            'success': True,
            'appointment': serializer.data
        })

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Appointment updated successfully!',
                'appointment': serializer.data
            })
        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appointment.delete()
        return Response({
            'success': True,
            'message': 'Appointment deleted successfully!'
        }, status=status.HTTP_204_NO_CONTENT)