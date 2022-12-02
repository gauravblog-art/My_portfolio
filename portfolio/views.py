from django.shortcuts import render
from portfolio.models import Contact, Blogs
from django.contrib import messages 

# Create your views here.
def home(request):
    return render(request, 'home.html')
def handleblog(request):
    
    posts=Blogs.objects.all()
    contex={"posts":posts}

    return render(request, 'blog.html',contex)
def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphone=request.POST.get("num")
        fdis=request.POST.get("desc")
        query=Contact(name=fname, email=femail, phone=fphone, description=fdis)
        query.save()
        messages.success(request, " Your form successfully submited")
          
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')