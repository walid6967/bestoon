from django.urls import path
from . import views

urlpatterns = [
    path('expense/create/', views.expense, name='create_expense'),
    path('income/create/', views.income, name='create_income'),
]
