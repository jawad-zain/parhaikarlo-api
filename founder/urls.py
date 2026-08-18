from django.urls import path
from .views import founder_dashboard

urlpatterns = [
    path('', founder_dashboard, name='founder-dashboard'),
]