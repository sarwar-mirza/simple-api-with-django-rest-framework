from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BusinessAutomationInterne

# Create your views here.
class InterneRegistrationTemplateView(TemplateView):
    template_name = 'enroll/interneregistration.html'
