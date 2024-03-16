from django.db import models

# Create your models(database) here.
class BusinessAutomationInterne(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dep = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    
