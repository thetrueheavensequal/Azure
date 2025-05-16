from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import EventType, Appointment, ContactMessage
from .forms import AppmntForm, ContactForm, ProfileForm


def home(request):
    return render(request, 'home.html')

def event_types(request):
    events = EventType.objects.all()
    return render(request, 'events.html', {'events': events})

@login_required(login_url='login')
def booking(request):
    if not request.user.is_authenticated:
        return render(request, 'users/not_logged_in.html')
    
    if request.method == 'POST':
        form = AppmntForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('status')  # or a success page
    else:
        form = AppmntForm()

    return render(request, 'booking.html', {'form': form})


@login_required(login_url='login')
def status(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-appmnt_on')
    latest = user_appointments.first() if user_appointments.exists() else None
    return render(request, 'status.html', {'appointment': latest})


def about(request):
    return render(request, 'about.html')


def contact(request):
    contact_info = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_info = form.save()
            form = ContactForm()  # Clear form after save
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {
        'form': form,
        'contact_info': contact_info
    })


def signup(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            error_message = "Username already taken. Please choose another."
        else:
            try:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('login')
            except:
                error_message = "An error occurred during signup. Please try again."

    return render(request, 'users/signup.html', {'error_message': error_message})


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
            error_message = "Invalid username or password."

    return render(request, 'users/login.html', {'error_message': error_message})


def logout(request):
    authlogout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please fix the errors in the form.")
    else:
        form = ProfileForm(instance=request.user)

    appointments = Appointment.objects.filter(user=request.user).order_by('-appmnt_date')
    return render(request, 'users/profile.html', {
        'form': form,
        'appointments': appointments
    })
