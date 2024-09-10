from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    context={'message':'Hello Braison'}
    return render(request,'index.html',context)

def signup(request):
    form=UserCreationForm()
    context={'form':form}
    return render(request,'signup.html',context)
