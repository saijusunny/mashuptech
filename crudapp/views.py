from django.shortcuts import render, redirect
from .models import *
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from django.contrib.auth.models import User,auth

# Create your views here.def 
from django.http import JsonResponse

def login(request):
    return render(request,'login.html')
def signup(request):
    
    return render(request, 'signup.html')



def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']
      
        if password != cpass:
            messages.info(request, 'Passwords do not match!!!!!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('signup')
        
        user=User.objects.create_user(
            first_name=fname,
            last_name=lname,
            username=username,
            password=password,
            email=email,
            
        )
        user.save()
        auth.login(request,user) 
        return redirect('home')

        
    else:
        return redirect('signup')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            if user.is_active:
                auth.login(request,user) 
                return redirect('home')
            else:
                return redirect('login')
                
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('login')
    else:
        return redirect('login')

def logout_view(request):
    logout(request)  # This logs out the user
    return redirect('login') 

@login_required
def home(request):
    tasks=task.objects.filter(user=request.user)
    tots=task.objects.filter(user=request.user).count()
  
    return render(request, "home.html",{'tasks':tasks,'tots':tots})
    
def edit_func(request):
    if request.method == 'POST':
        # Perform your logic here (e.g., saving data)
        ed_name= request.POST.get('ed_name')
        ed_task=request.POST.get('ed_task')
        ed_status=request.POST.get('ed_status')
        id=request.POST.get('id')
        
        edtask=task.objects.get(id=id)
        edtask.name=ed_name
        edtask.task_assign=ed_task
        edtask.complete=ed_status
        
        edtask.save()
        data={
            'status': 'success',
        }
        return JsonResponse(data)

    
    return redirect('home')

def add_func(request):
    if request.method == 'POST':
        
        addtask=task()
        addtask.name=request.POST.get('add_name')
        
        addtask.task_assign=request.POST.get('add_task')
        addtask.complete=request.POST.get('add_status')
        addtask.user=request.user
        addtask.save()
        data={
            'status': 'success',
        }
        return JsonResponse(data)

    
    return redirect('home')

def delete_fuc(request):
    key=request.GET.get('id')
    print(key)
    delt=task.objects.get(id=key).delete()
    data={
        'status': 'success',
    }
    return JsonResponse(data)





    
        
        
        
