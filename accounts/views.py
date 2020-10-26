
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/shop")
        else:
            messages.info(request,'Invalid Details')
            return redirect('login')

    else:

        return render(request, 'accounts/login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        email = request.POST.get('email', False)
        username = request.POST.get('username', False)
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)

        if password1==password2:
            if User.objects.filter(username = username ).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email id already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'Passwords dont match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')