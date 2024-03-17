from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BusinessAutomationInterneForm
from .models import BusinessAutomationInterne
from django.contrib import messages

# Create your views here.
class InterneRegistrationTemplateView(TemplateView):
    template_name = 'enroll/interneregistration.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = BusinessAutomationInterneForm()
        context = {'form':fm}
        return context


    def post(self, request):
        fm = BusinessAutomationInterneForm(request.POST)
        
        if fm.is_valid():
            fm.save()
            
            # message framework
            messages.success(request, 'Congratulations!!! your registration has been successfully.')
            fm = BusinessAutomationInterneForm()
            
        return render(request, 'enroll/interneregistration.html', {'form':fm})
