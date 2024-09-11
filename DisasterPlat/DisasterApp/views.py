from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def index(request):
    context={'message':'Hello Braison'}
    return render(request,'index.html',context)

def Register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Hello'+' '+ user+' '+'your account creation succesful')

            return redirect('login')

    context={'form':form}
    return render(request,'Register.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Please check your password or username")
    context={}
    return render(request,'login.html',context) 

def home(request):
    context={}
    return render(request,'home.html',context)
