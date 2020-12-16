from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from accounts.models import Userprofile, CustomUser
from accounts.forms import SignUpForm


def signup(request):  # TODO: Write test for this functionality
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
