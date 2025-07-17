from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def classes(request):
    return render(request, 'classes.html')

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

from .forms import AppointmentForm

def appointment(request):
    return render(request, 'appointment.html')

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