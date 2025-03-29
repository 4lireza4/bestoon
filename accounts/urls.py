from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework.routers import SimpleRouter


app_name = 'accounts'

router = SimpleRouter()
router.register('users', views.UserViewSet, basename='users')



urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('confirm-email/<key>/' , views.ConfirmEmailView.as_view(), name='confirm_email'),
    path('login/' , TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/' , TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

#
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzIxNzE2MSwiaWF0IjoxNzQzMTMwNzYxLCJqdGkiOiIzOTBiZDEwZjMwZTQ0NjIwODg0OGY5NTlhNGQ0ZDI2MCIsInVzZXJfaWQiOjF9._ZW_l90fswCRq2z3TnDLfzHtSyNuEoqGFifcwlzEAgw",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzMTMxMDYxLCJpYXQiOjE3NDMxMzA3NjEsImp0aSI6IjVmNmMxMTE4MjQwOTQ3YjBiM2IxNGVlZDE1NTNkYjExIiwidXNlcl9pZCI6MX0.NC7k5jZVsuJP-Ip5ACwtdBVGkNg7EY7k49DGK2BE5f8"
# }


