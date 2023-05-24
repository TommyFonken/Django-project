from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserChoice


def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def hosting(request):
    message = None
    if request.method == 'POST':
        option = request.POST['option']
        username = request.POST['username']
        hostname = request.POST['hostname']
        password = request.POST['password']
        if UserChoice.objects.filter(hostname=hostname).exists():
            message = f"Error hostname: {hostname} already exists."
        else:
            message = f"Success: {hostname} does not exist."
            UserChoice.objects.create(option=option, username=username, hostname=hostname, password=password)
    return render(request, 'users/hosting.html',{'error_message': message})