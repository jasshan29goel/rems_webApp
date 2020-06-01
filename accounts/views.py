from django.shortcuts import redirect, render

from django.contrib import  auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                # That username is taken
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # The email is being used
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            # password do not match    
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # logged in
            return redirect('dashboard')
        else:
            # invalid credentials
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request): 
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def dashboard(request):
    if request.user.is_authenticated==True:
        return render(request,'accounts/dashboard.html')
    else:
        return redirect('login')


