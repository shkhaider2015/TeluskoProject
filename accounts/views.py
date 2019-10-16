from django.shortcuts import render, redirect
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
            elif User.objects.filter(email=email):
                print('email is taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
                user.save()
                print('user created')
                return redirect('/')
        else:
            print("Password is not matching")


        

    else:
        return render(request, 'register.html')