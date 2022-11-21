from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_pass1=request.POST.get('pass1')
        get_pass2=request.POST.get('pass2')

        print(get_email)

    return render(request, 'signup.html')
def handlogin(request):
    return render(request, 'login.html')
def handlogout(request):
    return render(request, 'login.html')