from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request,'index.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.category = form.cleaned_data['category']
            user.save()
            # Your logic for successful registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')  # Replace 'dashboard' with the name or URL pattern of your dashboard view

        else:
            # Handle unsuccessful login
            return render(request, 'registration/login.html', {'error_message': 'Invalid Password or Username'})

    return render(request, 'registration/login.html')

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'index.html')
    