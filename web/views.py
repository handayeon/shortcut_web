from django.shortcuts import render
from .logic import *
from web.models import Shortcut
from django.core.paginator import Paginator



def index(request):
    if request.method == "POST":
        show_lists = Logic.get_list(request)
        return render(request, "web/index.html",{'short_lists': show_lists})
    return render(request, 'web/index.html')

def show_list(request):
<<<<<<< HEAD
    print("list")
    show_lists = Logic.get_list(request)
    return render(request, "web/list.html",{'short_lists': show_lists})
=======
    shortcut = Shortcut.objects.all()
    # paginator = Paginator(short_lists, 10) # Show 20 contacts per page
    # page = request.GET.get('page')

    return render(request, 'web/list.html', {'shortcut': shortcut})
>>>>>>> c45eace11bf9332fc9c96a5387c36c7b88e48166

def register(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/register.html',{"result":"fail"})

# def test(request):
    # print("test")
    # return Logic.get_list_test(request)
    # short_lists = Shortcut.objects.all()

    # paginator = Paginator(short_lists, 10) # Show 20 contacts per page

    # page = request.GET.get('page')
    # return render(request, 'web/test.html', {'short_lists': short_lists})
    
    