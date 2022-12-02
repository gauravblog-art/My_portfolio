from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_pass1=request.POST.get('pass1')
        get_pass2=request.POST.get('pass2')

        if get_pass1!=get_pass2:
            messages.info(request, "please enter same password")
            return redirect("/auth/signup/")
        # here we are cheking if the user already exist than we give the warning
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email i Taken")
        except Exception as identifier:
            pass
        # if the new user than we have to store the data into database

        myuser=User.objects.create_user(get_email,get_email, get_pass1)

        myuser.save()
        messages.success(request, "user sucefully created please login")
        return render(request, "login.html")

    return render(request, 'signup.html')

def handlogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_pass1=request.POST.get('pass1')
        myuser=authenticate(username=get_email, password=get_pass1)
        print(myuser)
       
        if myuser==None:
            # print("hello")
            messages.error(request, "invailed, credential")
        else:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect("/")
    return render(request, 'login.html')
def handlogout(request):

    logout(request)
    messages.success(request, "You logout success")
    return render(request, 'login.html')