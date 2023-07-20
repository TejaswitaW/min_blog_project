from django.shortcuts import render,HttpResponseRedirect

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
    return render(request,'blog/signup.html')

def user_login(request):
    return render(request,'blog/login.html')

def user_logout(request):
    return HttpResponseRedirect('/')