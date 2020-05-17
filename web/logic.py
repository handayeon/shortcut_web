from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.conf import settings
class Logic:
    def get_list(request):
        short_lists=None
        if request.method == "POST":
            print("post")
            count = 0
            os = request.POST['s1']
            program = request.POST['s2']
            searchValue = request.POST['searchValue']
            if os == "" and program == "":
                short_lists = Shortcut.objects.filter(action__icontains=searchValue)
            elif os == "":
                short_lists = Shortcut.objects.filter(program=program,action__icontains=searchValue)
            elif program == "":
                short_lists = Shortcut.objects.filter(os=os,action__icontains=searchValue)
            else : 
                short_lists = Shortcut.objects.filter(os=os, program=program,action__icontains=searchValue)
            for short_list in short_lists:
                print(short_list.num)
                count+=1
            if count == 0:
                short_lists=None
        else :
            print("get")
            short_lists = Shortcut.objects.order_by('num')
            #count = Shortcut.objects.count()
        return short_lists

    def register(request):
        os = request.POST['s1']
        program = request.POST['s2']
        action = request.POST['regRepValue']
        short = request.POST['regShortValue']
        short_lists = Shortcut.objects.create(os=os, program=program,action=action,short=short)
        result = 'success'
        print(result)
        return render(request,"web/register.html",{"result":result})
