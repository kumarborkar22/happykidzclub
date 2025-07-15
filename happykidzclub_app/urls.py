from .views import (
    index,
    about,
    classes,
    contact,
    facility,
    team,
    call_to_action,
    appointment,
    testimonial,
    error_404,
    gallery,

    contact_messages_api,
)

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('classes/', classes, name='classes'),
    path('contact/', contact, name='contact'),
    path('facility/', facility, name='facility'),
    path('team/', team, name='team'),
    path('call-to-action/', call_to_action, name='call-to-action'),
    path('appointment/', appointment, name='appointment'),
    path('testimonial/', testimonial, name='testimonial'),
    path('404/', error_404, name='404'),
    path('gallery/', gallery, name='gallery'),

    path('api/contact-messages/', contact_messages_api, name='contact_messages_api'),

]