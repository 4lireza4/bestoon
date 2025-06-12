from django.db.models import Sum
from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExpenseForm , IncomeForm
from web.models import Expense, Income
from django.contrib import messages

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


class AddExpenseView(View):
    form_class = ExpenseForm
    template_name = "add_expense.html"
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "خرج جدید با موفقیت ثبت شد!" , 'success')
            return redirect("client_web:dashboard")  # تغییر بده به اسم صفحه داشبوردت
        return render(request, self.template_name, {"form": form})


class AddIncomeView(LoginRequiredMixin , View):
    form_class = IncomeForm
    template_name = "add_income.html"
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, "درآمد جدید با موفقیت ثبت شد!" , 'success')
            return redirect("client_web:dashboard")
        return render(request, self.template_name, {"form": form})

    