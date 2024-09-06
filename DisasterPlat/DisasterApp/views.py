from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={'message':'Hello Braison'}
    return render(request,'index.html',context)
