from django.shortcuts import render
from .logic import *

def index(request):
    if request.method == "POST":
        show_lists = Logic.get_list(request)
        return render(request, "web/index.html",{'short_lists': show_lists})
    return render(request, 'web/index.html')

def show_list(request):
    print("list")
    show_lists = Logic.get_list(request)
    return render(request, "web/list.html",{'short_lists': show_lists})

def register(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/register.html',{"result":"fail"})

