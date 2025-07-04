from django import forms
from accounts.models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['email', 'username']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            user = user_qs.first()
            if not user.is_active :
                raise forms.ValidationError(
                    "این ایمیل قبلاً ثبت‌نام کرده ولی هنوز فعال نشده. "
                    "لطفاً ایمیل خود را بررسی کنید یا درخواست ارسال مجدد لینک تأیید کنید."
                )
            else:
                raise forms.ValidationError("این ایمیل قبلاً ثبت‌نام کرده است.")
        return email


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user



class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=254, label="Email" , widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))



class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }