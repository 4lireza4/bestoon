from django.contrib import admin
from web.models import Expense, Income


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title' , 'user' , 'amount' , 'created' , 'updated')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title' , 'user' , 'amount' , 'created' , 'updated')