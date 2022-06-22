from typing import Match
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.models import User,auth
from django.http.response import Http404, HttpResponse

# Create your views here.
def register(request):
    if request.method =='POST':
        fname = request.POST['fname']
        last_name = request.POST['last_name']
        uname = request.POST['uname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
          if User.objects.filter(username=uname).exists():
              messages.info(request,'username taken')
              print(" username  taken ")
              return redirect('register')
          elif User.objects.filter(email=email).exists():
              messages.info(request,'email taken')
              print('email taken')  
              return redirect('register') 
          else:    
           user= User.objects.create_user(username=uname,password=password1,email=email,first_name=fname)
           user.save()
           print("user created")
           return redirect("login")
           
        else:
            print("password not matching....")
            return redirect ('register')
        return redirect("/")
 
        
    else:
        return render (request,"register.html")




def login(request): 
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']

        user =auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            print ("invalid credentials")
            return redirect('login')    
    else:   
        return render (request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')