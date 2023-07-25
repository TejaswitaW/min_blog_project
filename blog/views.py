from django.shortcuts import render,HttpResponseRedirect
from .forms import UserSignUpForm,UserLoginForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    return render(request,'blog/dashboard.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!!! You have become an Author.")
            form.save()
    else:
        form = UserSignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    form = UserLoginForm()
    return render(request,'blog/login.html',{'form':form})

def user_logout(request):
    return HttpResponseRedirect('/')