from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'],
                                     first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        return redirect('home:home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
