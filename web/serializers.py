from rest_framework import serializers
from .models import Expense, Income


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id' ,'user'  ,  'title' , 'amount'  , 'created' , 'updated')
        read_only_fields = ('id' ,'user' , 'created' , 'updated')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id' ,'user' , 'title' , 'amount' , 'created' , 'updated')
        read_only_fields = ('id' ,'user' , 'created' , 'updated')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)   
