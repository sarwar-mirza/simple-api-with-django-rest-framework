from django.contrib import admin
from .models import BusinessAutomationInterne

# Register your models here.
@admin.register(BusinessAutomationInterne)
# create class
class BusinessAutomationInterneAdmin(admin.ModelAdmin):
    # Ordering table field name
    list_display = ['id', 'first_name', 'last_name', 'dep', 'city', 'email']
