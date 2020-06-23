from datetime import datetime,timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .models import Contact

# Create your views here.


@csrf_protect
def login(request,):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['pass']
        from django.contrib import auth
        user=auth.authenticate(username=a,password=b,date=datetime.today())
        if user is None:
            return render(request,'index.html')
        else:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('indexx'))

    else:
            return render(request, "index.html")
      # return HttpResponse('kkkkkkkkkkk')
     # return render(request,"index.html")
@login_required(login_url='/')
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return redirect('/')
@login_required(login_url='/')
def indexx(request):
    return render(request,"indexx.html")

@login_required(login_url='/')
def photos(request):
   return render(request,"photos.html")

@login_required(login_url='/')
def bio(request):
   return render(request,"bio.html")

@login_required(login_url='/')
def blog(request):
   return render(request,"blog.html")

@login_required(login_url='/')
def contact(request):
    if request.method == 'POST':
        a=request.POST['fname']
        b=request.POST['lname']
        c = request.POST['email']
        d = request.POST['sub']
        x=Contact(First_Name=a,Last_Name=b,Email_Id=c,Subject=d)
        x.save()
        print('Success')
        return render(request,'indexx.html')
    else:
      return render(request,"contact.html")


@login_required(login_url='/')
def single(request):
   return render(request,"single.html")

def signup(request):
    if request.method == 'POST':
       a=request.POST['username']
       b = request.POST['name']
       c = request.POST['email']
       d = request.POST['password']
       e = request.POST['cpassword']
       if d == e:
         x=User.objects.create_user(username=a,first_name=b,email=c,password=d)
         x.save()
         print('success')
         return redirect('/')
       else:
           return render(request,'signup.html',{'error':'password and confirm password not matched'})
    else:
        return render(request,'signup.html')