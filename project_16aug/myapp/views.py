from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import login

# Create your views here.

def members(request):
    return HttpResponse("Hello world!")

def loginn(request):
    if request.method == 'POST':
        # print(request.POST)
        Username_name = request.POST.get('Username')
        Password = request.POST.get('Password')
        
        l1 = [Username_name , Password]
        print(l1)
        log = login(Username = Username_name, Password = Password )
        log.save()
        
        return render(request, 'login.html',{})
    else:
        return render(request, 'login.html',{})

# def login_view(request):
#     # print(request.POST)
#     return render(request, 'login.html')