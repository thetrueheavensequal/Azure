from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin, logout as authlogout
from django.contrib.auth.decorators import login_required
from home.models import Appointment
from home.forms import ProfileForm

# Create your views here.
def signup(request):
    error_message = None
    created_user = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            error_message = "Username already taken. Please choose another."
        else:
            try:
                created_user = User.objects.create_user(username=username, password=password)
                return redirect('login')  # redirect to login after successful sign up
            except Exception as e:
                error_message = "An error occurred during signup. Please try again."

    return render(request, 'users/signup.html', {
        'error_message': error_message,
        'User': created_user
    })


def login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            authlogin(request, user)
            return redirect('home')
        else:
            error_message = "Invalid credentials"

    return render(request, 'users/login.html', {'error_message': error_message})

def logout(request):
    authlogout(request)
    return redirect('home')


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # or whatever your profile URL name is
    else:
        form = ProfileForm(instance=user)

    appointments = Appointment.objects.filter(user=user).order_by('-appmnt_date')
    return render(request, 'users/profile.html', {
        'form': form,
        'appointments': appointments
    })