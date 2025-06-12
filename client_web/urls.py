from django.urls import path
from . import views

app_name = 'client_web'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path("add-expense/", views.AddExpenseView.as_view(), name="add_expense"),
    path("add-income/", views.AddIncomeView.as_view(), name="add_income")
]