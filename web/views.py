from django.shortcuts import render
from .logic import *
from web.models import Shortcut
from django.core.paginator import Paginator



def index(request):
    return render(request, 'web/index.html')

def show_list(request):
    shortcut = Shortcut.objects.all()
    # paginator = Paginator(short_lists, 10) # Show 20 contacts per page
    # page = request.GET.get('page')

    return render(request, 'web/list.html', {'shortcut': shortcut})

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
    
    