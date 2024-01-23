from django import forms


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)
