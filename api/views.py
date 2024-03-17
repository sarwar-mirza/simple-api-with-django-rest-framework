from django.shortcuts import render
from rest_framework import viewsets
from enroll.models import BusinessAutomationInterne
from .serializers import BusinessAutomationInterneSerializers

# Create your views here.
class BusinessAutomationInterneModelViewSets(viewsets.ModelViewSet):
    
    queryset = BusinessAutomationInterne.objects.all()  # Retrieve all instances of MyModel from the database
    serializer_class = BusinessAutomationInterneSerializers  # Convert [python data to json data]
