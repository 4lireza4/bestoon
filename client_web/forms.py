from datetime import datetime

from django import forms
from web.models import Expense, Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["title","description", "amount" , "date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "عنوان خرج"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "توضیحات"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "مبلغ"}),
            "date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "زمان",
                    "type": "datetime-local"  # این خیلی مهمه برای مرورگر
                },
                format="%Y-%m-%dT%H:%M"  # فرمت ورودی datetime-local
            ),
        }




class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["title", "description", "amount", "date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "عنوان درآمد"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "توضیحات"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "مقدار"}),
            "date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "تاریخ و زمان",
                    "type": "datetime-local"
                },
                format="%Y-%m-%dT%H:%M"
            ),
        }


