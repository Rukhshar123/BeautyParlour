from django.shortcuts import render,redirect
from adminservice.models import *
from django.contrib import messages
import datetime
import hashlib
from .models import *
from django.contrib.sessions.models import Session
from django.http import HttpResponse, response
from datetime import datetime

def home(request):
    service = Service.objects.all
    news = LatestNews.objects.all
    review = Reviews.objects.all
    brand = Brands.objects.all
    return render(request,'index.html',{'service':service,'news':news,'review':review,'brand':brand})

def about(request):
    about = About.objects.last
    team = Team.objects.all
    review = Reviews.objects.all
    brand = Brands.objects.all
    #print(about)
    return render(request,'about.html',{'about':about,'team':team,'review':review,'brand':brand})

def services(request):
    service = Service.objects.all
    review = Reviews.objects.all
    brand = Brands.objects.all
    return render(request,'services.html',{'service':service,'review':review,'brand':brand})

def blog(request):
    blog = Blog.objects.all
    return render(request,'blog.html',{'blog':blog})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']

        obj = Contact(name=name,phone=phone,message=message)
        obj.save()

        messages.success(request,"Message sent successfully!!")
        return redirect('contact')
    return render(request,'contact.html')

def service_page(request):
    service = Service.objects.all
    return render(request, 'services-page.html',{'service':service})

def appoinment(request):
    if request.method == 'POST':
       """ name = request.POST['name']
        phone = request.POST['phone']
        sdate = request.POST['startdate']
        startdate = datetime.strptime(sdate, "%d/%m/%Y").strftime("%Y-%m-%d")
        print(startdate)
        edate = request.POST['enddate']
        enddate = datetime.strptime(edate, "%d/%m/%Y").strftime("%Y-%m-%d")
        print(enddate)
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        message = request.POST['message']
        user_id = request.POST['user_id']"""

       name = request.POST['name']
       phone = request.POST['phone']
       date = request.POST['date']
       appdate = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
       time = request.POST['time']
       message = request.POST['message']
       user_id = request.POST['user_id']
       obj = Appoinment(name=name,phone=phone,date=appdate,time=time,message=message)
       obj.userid_id = user_id
       obj.save()
       messages.success(request,"Appoinment has placed Successfully")
       return redirect('appoinment')

    return render(request, 'appoinments.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        cpw = request.POST['conf_password']
        cpwd = hashlib.md5(cpw.encode())
        conf_password = cpwd.hexdigest()

        if Register.objects.filter(email=email):
            messages.error(request, "Email Already Exist!! Please login")
        else:
            if password==conf_password:
                obj = Register(name=name,phone=phone,email=email,password=password)
                obj.save()
                messages.success(request,"Registration successful!! Please Login")
                return redirect('login')

            else:
                messages.error(request, "Password and confirm password should be same")

def login(request):
    if request.session.has_key('Is_Login'):
        return redirect('appoinment')

    if request.method == 'POST':
        email = request.POST['email']
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        count = Register.objects.filter(email=email, password=password).count()
        if count > 0:
            request.session['Is_Login'] = True
            request.session['user_id'] = Register.objects.values('id').filter(email=email, password=password)[0]['id']
            return redirect('appoinment')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')

def sidebar(request,id):
    user = Register.objects.get(id=id)
    return render(request, 'sidebar.html', {'user': user})

def show_profile(request):
    id=request.session.get('user_id')
    user = Register.objects.filter(id=id)
    print("user id ",id)
    return render(request, 'show_profile.html',{'user':user})

def editProfile(request):
    id=request.session.get('user_id')
    user = Register.objects.get(id=id)
    return render(request,'editProfile.html',{'user':user})

def updateProfile(request):
    id = request.session.get('user_id')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        if Registration.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exist!! Please login")
        else:
            Register.objects.filter(id=id).update(name=name, email=email, phone=phone)

        messages.success(request,"Profile updated Successfully")
        return redirect('show_profile')

def changePassword(request):
    id = request.session.get('user_id')
    if request.method == 'POST':
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        cpw = request.POST['conf_password']
        cpwd = hashlib.md5(cpw.encode())
        conf_password = cpwd.hexdigest()

        if password == conf_password:
            Register.objects.filter(id=id).update(password=password)
            messages.success(request,"Password Updated successfully")
            return redirect('show_profile')
        else:
            messages.error(request, "Password and confirm password should be same")

    return render(request,'changePassword.html')


def signout(request):
   del request.session['Is_Login']
   return redirect('home')

def user_get_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        if Register.objects.filter(email=email):
            request.session['email'] = email
            return redirect('user_forgot_password')
        else:
            messages.error(request, 'email is incorrect')
    return render(request, 'user_get_email.html')

def user_forgot_password(request):
    email = request.session['email']
    print(email)
    if request.method == 'POST':
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        cpw = request.POST['conf_password']
        cpwd = hashlib.md5(cpw.encode())
        conf_password = cpwd.hexdigest()

        if password == conf_password:
            Register.objects.filter(email=email).update(password=password)
            messages.success(request, "Password Updated successfully")
            return redirect('login')
        else:
            messages.error(request, "Password and confirm password should be same")

    return render(request, 'user_forgot_password.html')


