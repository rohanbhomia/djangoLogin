from django.shortcuts import render
from users.forms import CustomUserCreationForm
from users.models import CustomUser
from django.contrib.auth import login


# Create your views here.


def register(request):

    context = {}
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password1')

            user = CustomUser.objects.create_user(
                email=email,
                password=password)

            login(request, user)

            print("sign up successfully...")
        else:
            print("not valid...", form.errors)

        return render(request, "register/register.html", {'form': form})

    return render(request, "register/register.html", {'form': form})
