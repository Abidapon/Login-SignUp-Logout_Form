from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from . forms import SignupForm
# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    return render(request, 'login.html')

def SignupPage(request):
    form= SignupForm()
    if request.method=='POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User has been created successfully")
    context= {
        'form': form
    }
    return render(request, 'signup.html', context)