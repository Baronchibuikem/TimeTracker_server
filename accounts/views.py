from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
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


@login_required
def user_edit_profile(request):
    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name", '')
        request.user.last_name = request.POST.get("last_name", '')
        request.user.email = request.POST.get("email", '')
        request.user.save()
        messages.success(request, 'Profile details updated.')
        return redirect("myaccount")
    return render(request, "accounts/editprofile.html")
