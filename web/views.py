# from django.shortcuts import render
# from .logic import *
# from .models import Shortcut
# from django.core.paginator import Paginator

# def show_list(request):
#     shortcuts = Shortcut.objects 
#     short_list = Shortcut.objects.all()
#     # paginator = Paginator(shortcuts, 10) # Show 20 contacts per page
#     # page = request.GET.get('page')
#     shortcut_lists = paginator.get_page(page)

#     return render(request, 'web/list.html', {'shortcuts': shortcuts}, {'short_lists': short_lists})

# def register(request):
#     if request.method == "POST":
#         return Logic.register(request)
#     return render(request, 'web/register.html',{"result":"fail"})

# # def test(request):
#     # print("test")
#     # return Logic.get_list_test(request)
#     # short_lists = Shortcut.objects.all()

#     # paginator = Paginator(short_lists, 10) # Show 20 contacts per page

#     # page = request.GET.get('page')
#     # return render(request, 'web/test.html', {'short_lists': short_lists})
    
from django.shortcuts import render
from .logic import *
from .models import Shortcut
from django.core.paginator import Paginator


def index(request):
    if request.method == "POST":
        show_lists = Logic.get_list(request)
    return render(request, 'web/index.html')

def show_list(request):
    print("list")
    show_lists = Logic.get_list(request)
    paginator = Paginator(show_lists, 10)
    return render(request, "web/list.html",{'short_lists': show_lists})

    

def register(request):
    if request.method == "POST":
        return Logic.register(request)
    return render(request, 'web/register.html',{"result":"fail"})

