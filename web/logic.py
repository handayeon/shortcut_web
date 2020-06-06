from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.conf import settings
class Logic:
    def get_list(request):
        count = 0 
        short_lists=None
        if request.method == "POST":#검색 시
            os = request.POST['s1']
            program = request.POST['s2']
            searchValue = request.POST['searchValue']
            request.session['os'] = os
            request.session['program'] = program
            request.session['searchValue'] = searchValue
            short_lists, count=Logic.get_logic(os, program, searchValue,count)#get_list에서 값 가져오기
        else :
            if request.session.get('os', False) or request.session.get('program', False) or request.session.get('searchValue', False):#검색하고 2번으로 넘어갈 때
                os = request.session['os']
                program = request.session['program']
                searchValue = request.session['searchValue']
                short_lists, count=Logic.get_logic(os, program, searchValue,count)
            else:#검색 아예 안 했을 때
                short_lists = Shortcut.objects.order_by('num')
                count = Shortcut.objects.count()
        return short_lists

    def register(request):#등록
        os = request.POST['s1']
        program = request.POST['s2']
        action = request.POST['regRepValue']
        short = request.POST['regShortValue']
        short_lists = Shortcut.objects.create(os=os, program=program,action=action,short=short)
        result = 'success'
        print(result)
        return render(request,"web/register.html",{"result":result})

    def get_logic(os, program, searchValue, count):#filter해서 값 가져오기
        short_lists = None
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
        return short_lists, count