
from django.http import HttpResponse
from .forms import AccountAuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)


# Create your views here.


def home(request):

    return render(request, "login/home.html", {})


def login_page(request):

    context = {}
    user = request.user
    # if user.is_authenticated:
    #     return redirect("home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home")
        else:
            messages.error(request, "please Correct Below Errors")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, "login/login.html", context)


def logout(request):

    return redirect('login')
