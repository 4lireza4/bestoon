from django.shortcuts import render,  redirect
from django.views import View
from .forms import RegisterForm , UserLoginForm , UserProfileEditForm
from .utils import send_confirmation_email
from django.contrib import messages
from accounts.models import User , EmailConfirmation
from django.contrib.auth import authenticate, login , logout
from web.models import Income , Expense
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class UserRegisterView(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'شما قبلاً وارد شده‌اید.' , 'info')
            return redirect('client_web:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()

        return render(request , self.template_name ,{'form':form} )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            send_confirmation_email(user)
            messages.success(request, 'Verification email sent. Check your inbox.')
            return redirect('client_accounts:login')
        return render(request , self.template_name ,{'form':form})

class ConfirmEmail(View):
    template_name = 'accounts/confirm_email.html'
    def get(self , request, key):
        try:
            confirmation = EmailConfirmation.objects.get(key=key)
            if confirmation.confirm():
                return render(request, self.template_name, {'message': 'Email confirmed. You can now log in.'})
            return render(request, self.template_name, {'error': 'Invalid or expired key.'})
        except EmailConfirmation.DoesNotExist:
            return render(request, self.template_name, {'error': 'Invalid key.'})


class UserLoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'شما قبلاً وارد شده‌اید.' , 'info')
            return redirect('client_web:home')
        return super().dispatch(request, *args, **kwargs)

    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    def get(self, request):
        form = self.form_class()
        return render(request , self.template_name ,{'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد حساب کاربری خود شدید.', 'info')
                return redirect('client_web:home')
            messages.error(request , 'ایمیل یا پسوورد اشتباه است.', 'danger')
        return render(request , self.template_name ,{'form':form})

class UserLogoutView(LoginRequiredMixin , View):
    def get(self, request):
        logout(request)
        messages.success(request, 'شما با موفقیت از حساب کاربری خود خارج شدید.', 'success')
        return redirect('client_web:home')


class UserProfileView(LoginRequiredMixin , View):
    template_name = 'accounts/profile.html'
    def get(self , request):
        user = request.user
        return render(request , self.template_name ,{'user':user})



class UserProfileEditView(LoginRequiredMixin , View):
    template_name = 'accounts/edit_profile.html'
    form_class = UserProfileEditForm
    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request , self.template_name ,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request ,"پروفایل شما با موفقیت بروزرسانی شد." , 'success')
            return redirect('client_accounts:profile')
        return render(request , self.template_name ,{'form':form})

class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('client_accounts:reset_password_done')
    email_template_name = 'accounts/password_reset_email.html'


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('client_accounts:password_reset_complete')

class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_compete.html'


