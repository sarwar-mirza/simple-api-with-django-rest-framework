from rest_framework import serializers
from enroll.models import BusinessAutomationInterne

class BusinessAutomationInterneSerializers(serializers.ModelSerializer):
    class Meta:
        model = BusinessAutomationInterne  # database connect
        # ordering field name
        fields = ['id', 'first_name', 'last_name', 'dep', 'city', 'email']