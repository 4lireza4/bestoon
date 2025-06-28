from django.db.models import Sum
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExpenseForm , IncomeForm
from web.models import Expense, Income
from django.contrib import messages
from django.views.generic import CreateView , TemplateView
from django.urls import reverse , reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        expenses = Expense.objects.filter(user=user).order_by('-created')
        incomes = Income.objects.filter(user=user).order_by('-created')

        total_expense = expenses.aggregate(total_expense=Sum('amount'))['total_expense'] or 0
        total_income = incomes.aggregate(total_income=Sum('amount'))['total_income'] or 0

        context.update({
            'expenses': expenses,
            'incomes': incomes,
            'total_expense': total_expense,
            'total_income': total_income
        })

        return context


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