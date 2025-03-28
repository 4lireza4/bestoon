from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('expense' , views.ExpenseViewSet , basename='expense')
router.register('income' , views.IncomeViewSet , basename='income')



app_name = 'web'
urlpatterns = [

] + router.urls