from django.shortcuts import render , HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Expense , Income
from .serializers import ExpenseSerializer, IncomeSerializer
from rest_framework.viewsets import ModelViewSet


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)