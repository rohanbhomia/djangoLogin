from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm
from users.models import CustomUser
from django.contrib.auth import login
from login.views import home, login_page, login
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.


def register(request):

    form = CustomUserCreationForm()

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = CustomUserCreationForm(
            request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password1')
            username = request.POST.get('username')

            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                username=username,
            )

            messages.success(request, "Sign up successfully")
            return redirect('login')
        else:
            print("not valid...", form.errors)
            print("not validaaa...", form.cleaned_data['username'])
            username = form.cleaned_data['username']
            if form.cleaned_data.get('email') is not None:
                email = form.cleaned_data['email']
            else:
                email = ''
            return render(request, "register/register_v2.html", {'form': form, 'not_valid': True, 'username': username, 'email': email})

    return render(request, "register/register_v2.html", {'form': form})


def username_check(request):
    username = request.POST.get('username')
    customuser_obj = CustomUser.objects.filter(username=username)
    if customuser_obj:
        return HttpResponse('True')
    else:
        return HttpResponse('False')


def email_check(request):
    email = request.POST.get('email')
    customuser_obj = CustomUser.objects.filter(email=email)
    if customuser_obj:
        return HttpResponse('True')
    else:
        return HttpResponse('False')
