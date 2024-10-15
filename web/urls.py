from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense, name='home'),  # Example URL
]
