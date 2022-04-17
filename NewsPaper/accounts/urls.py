from django.urls import path
from .views import ProfileUpdateView, ProfileDetail


urlpatterns = [
   path('', ProfileDetail.as_view(), name='account'),
   path('edit/', ProfileUpdateView.as_view(), name='account_edit'),
]