from django.urls import path
from enroll import views

# route (backends file)
urlpatterns = [
    path('', views.InterneRegistrationTemplateView.as_view(), name='home-page'),
]
