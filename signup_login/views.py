from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import signup_form,formss,addhouse
from .models import house
from django.contrib.auth import authenticate,login,logout
def index(request):
    
    return render(request,'user-new.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('signup_login:home'))
@login_required
def addhouse1(request):
    if request.method=="POST":
        ahform=addhouse(data=request.POST)
        if ahform.is_valid:
            ahform.save()
            return HttpResponseRedirect(reverse('signup_login:home'))
        else:
            print(ahform.errors)
    else:
        ahform=addhouse()
        return render(request,'addHouse.html',{'form':ahform})

def register(request):
    registered=False
    if request.method=='POST':
        form=signup_form(data=request.POST)
        formsss=formss(data=request.POST)
        if form.is_valid() and formsss.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            profile=formsss.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
            return HttpResponseRedirect(reverse('signup_login:home'))
        else:
            print(form.errors)
            print(formsss.errors)
            return HttpResponse('invalid signup')
    else:
        form=signup_form()
        formsss=formss()
    return render(request,'login-new.html',{
        'form':form,
        'formsss':formsss,
        'registered':registered,
        'signup':True,
        
    })
def user_login(request):
    if request.method=='POST':
        un=request.POST.get('username_login')
        pwd=request.POST.get('password_login')
        user=authenticate(username=un,password=pwd)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('signup_login:home'))
            else:
                return HttpResponse('account not active')
        else:
            return HttpResponse('invalid login!')  
    else:
        return render(request,'login-new.html',{'login':True})
def search(request):
    ob=house.objects.all()
    return render(request,'search.html',{'houses':ob})
