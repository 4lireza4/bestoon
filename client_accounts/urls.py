from django.urls import path
from . import views

app_name = 'client_accounts'

urlpatterns = [
    path('register/' , views.UserRegisterView.as_view(), name='register'),
    path('register/confirm-email/<key>/' , views.ConfirmEmail.as_view(), name='confirm_email'),
    path('login/' , views.UserLoginView.as_view(), name='login'),
    path('logout/' , views.UserLogoutView.as_view(), name='logout'),
    path('profile/' , views.UserProfileView.as_view(), name='profile'),
    path('profile/edit/' , views.UserProfileEditView.as_view(), name='profile_edit'),
    path('reset_password/' , views.UserPasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/' , views.UserPasswordResetDoneView.as_view(), name='reset_password_done'),
    path('confirm/<uidb64>/<token>/' , views.UserPasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('confirm/complete/' , views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]