from django.shortcuts import render
from .logic import *

def index(request):
    return render(request, 'web/index.html')

def show_list(request):
    print("list")
    return Logic.get_list(request)

def register(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/register.html',{"result":"fail"})

