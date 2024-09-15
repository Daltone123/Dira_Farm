from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

#Homepage
def home_dira(request):
    return render(request, 'index.html')

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home_dira')  # Redirect to a home page or another appropriate page
        else:
            messages.error(request, 'Error registering user.')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'register_form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home_dira')  # Redirect to a home page or another appropriate page
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'login_form': form})
