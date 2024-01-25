from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این کاربر از قبل وجود دارد')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود دارد')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('رمز عبورها یکسان نیستند')
        elif len(confirm_password) < 8:
            raise forms.ValidationError('رمز عبور حداقل باید 8 کاراکتر باشد')
        elif not any(x.isupper() for x in confirm_password):
            raise forms.ValidationError('رمز عبور باید حداقل شامل یک حرف بزرگ باشد')
        return confirm_password


class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
