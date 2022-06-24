from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'pages/register.html',locals())

def login(request):
    return render(request,'pages/login.html',locals())

def logout(request):
    return render(request,'pages/logout.html',locals())