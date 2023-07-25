from django.shortcuts import render,HttpResponseRedirect
from .forms import UserSignUpForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

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
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserLoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user != None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!')
                    return HttpResponseRedirect('/dashboard/')

        else:
            form = UserLoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')