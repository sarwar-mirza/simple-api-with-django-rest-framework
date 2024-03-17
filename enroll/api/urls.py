from django.urls import path, include
from rest_framework.routers import DefaultRouter


# package.folder_name import views
from enroll.api import views

# create router
router = DefaultRouter()

# Register BusinessAutomationInterneModelViewSets with router
router.register('interneapi', views.BusinessAutomationInterneModelViewSets, basename='interne')


urlpatterns = [
    path('', include(router.urls)),
]
