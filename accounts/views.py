from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= user_name, password=password)

        if user is not None:
            print("User is not None")
            auth.login(request, user)
            return redirect("/")
        else:
            print("User is  None ???")
            messages.info(request, "Invalid Credential")
            return redirect("login")
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            print('Password is matching')
            if User.objects.filter(username=user_name).exists():
                print('username is taken')
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                print('email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print("Password is not matching")
            messages.info(request, 'Password is not matching')
            return redirect('register')


        

    else:
        return render(request, 'register.html')

def logout(request):
    print("logout Done ...!")
    auth.logout(request)
    return redirect("/")