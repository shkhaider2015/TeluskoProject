from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

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
            if User.objects.filter(username=user_name).exist():
                print('username is taken')
                return redirect('register')
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email taken')
                print('email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
                user.save()
                print('user created')
                return redirect('/')
        else:
            print("Password is not matching")
            messages.info(request, 'Password is not matching')
            return redirect('register')


        

    else:
        return render(request, 'register.html')