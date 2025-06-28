from django.shortcuts import redirect
from django.contrib import messages

class AnonymousRequiredMixin:
    redirect_url = 'client_web:home'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'شما قبلاً وارد شده‌اید.', 'info')
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
