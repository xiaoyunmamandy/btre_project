from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'that username is exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'that email is used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save()
                    messages.success(request,'you are now registered and can login')
                    return redirect('login')

        else:
            messages.error(request,'password donnot match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now login')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('111')
        messages.success(request,'you are now logout')
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')