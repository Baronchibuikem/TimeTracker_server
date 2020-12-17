from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from accounts.models import Userprofile, CustomUser
from accounts.forms import SignUpForm


def user_signup(request):  # TODO: Write test for this functionality
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            userprofile = Userprofile.objects.create(user=new_user)
            login(request, new_user)
            return redirect('frontpage')

    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('frontpage')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('myaccount')
        else:
            return HttpResponse("Invalide login credentials")

    return render(request, 'accounts/login.html')
