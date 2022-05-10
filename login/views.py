
from django.http import HttpResponse
from .forms import AccountAuthenticationForm, ChangePassword
from django.contrib.auth import login, logout as django_logout, authenticate
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from users.models import CustomUser
import random
from django.core.mail import send_mail


# Create your views here.


def home(request):
    user = request.user

    return render(request, "login/home.html", {'user': user})


def login_page(request):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = AccountAuthenticationForm(
            request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home")
        else:
            messages.error(request, "Please correct below errors")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, "login/login.html", context)


def logout(request):
    django_logout(request)
    return redirect('login')


def forgot_password(request):
    if request.POST:
        email = request.POST.get('email')
        custom_user_obj = CustomUser.objects.filter(email=email).exists()
        if custom_user_obj:
            otp = random.randint(0000, 9999)
            custom_user_obj = CustomUser.objects.get(email=email)
            custom_user_obj.otp = otp
            custom_user_obj.save()

            send_mail(
                'Subject here',
                f'otp is {otp}',
                'rkhobragade5995@gmail.com',
                ['rkhobragade5995@gmail.com'],
            )
            print('otp...', otp)
            return render(request, "login/reset_password.html", {'reset': True, 'email': email})
        else:
            return render(request, "login/reset_password.html", {'message': 'Invalid email', 'invalid': True})
    else:
        return render(request, "login/reset_password.html", {})


def otp_check(request):
    otp = request.POST.get('otp')
    email = request.POST.get('email')
    custom_user_obj = CustomUser.objects.filter(email=email, otp=otp).exists()
    if custom_user_obj:

        form = ChangePassword()
        return render(request, "login/reset_password.html", {'otp': True, 'form': form, 'email': email})
    else:

        return render(request, "login/reset_password.html", {'reset': True, 'email': email, 'message': 'Invalid otp', 'invalid': True})


def save_password(request):
    form = ChangePassword(request.POST)
    password1 = request.POST.get('password1')
    email = request.POST.get('email')

    if form.is_valid():
        custom_user_obj = CustomUser.objects.get(email=email)
        custom_user_obj.set_password(password1)
        custom_user_obj.save()

        messages.success(request, "Password reset successfully")
        return redirect('login')

    else:

        return render(request, "login/reset_password.html", {'otp': True, 'form': form, 'email': email})
