from django.db.models import Sum
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExpenseForm , IncomeForm
from web.models import Expense, Income
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse , reverse_lazy


class HomeView(View):
    def get(self , request):
        return render(request, 'home.html')



class DashboardView(LoginRequiredMixin , View):
    def get(self , request):
        expenses = Expense.objects.filter(user=request.user).order_by('-created')
        incomes = Income.objects.filter(user=request.user).order_by('-created')

        total_expense = expenses.aggregate(total_expense=Sum('amount'))['total_expense'] or 0
        total_income = incomes.aggregate(total_income=Sum('amount'))['total_income'] or 0

        context = {
            'expenses': expenses,
            'incomes': incomes,
            'total_expense': total_expense,
            'total_income': total_income
        }

        return render(request , 'dashboard.html' , context=context)


class AddExpenseView(LoginRequiredMixin , CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'add_expense.html'
    success_url = reverse_lazy('client_web:dashboard')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        messages.success(self.request, "خرج جدید با موفقیت ثبت شد!" , 'success')
        return super().form_valid(form)


class AddIncomeView(LoginRequiredMixin , CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'add_income.html'
    success_url = reverse_lazy('client_web:dashboard')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        messages.success(self.request, "درآمد جدید با موفقیت ثبت شد!" , 'success')
        return super().form_valid(form)