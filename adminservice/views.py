from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib import messages
from .models import *
import hashlib
from django.contrib.sessions.models import Session
from userservices.models import *


def admin_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        speciality = request.POST['speciality']
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        cpw = request.POST['conf_password']
        cpwd = hashlib.md5(cpw.encode())
        conf_password = cpwd.hexdigest()

        if Registration.objects.filter(email=email).exists():
            messages.error(request, "Email Already Exist!! Please login")
        else:
            if password == conf_password:
                obj = Registration(name=name, email=email, contact=contact, speciality=speciality, password=password)
                obj.save()
                messages.success(request,"Regsiter Successfully,Please login")
                return redirect('admin_login')
            else:
                messages.error(request, "Password and confirm password should be same")


    return render(request, 'admin_register.html')


def admin_login(request):
    if request.session.has_key('Is_Login'):
        return redirect('admin_home')

    if request.method == 'POST':
        email = request.POST['email']
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        id = Registration.objects.filter(email=email, password=password).values_list("id")
        if id:
            request.session['Is_Login'] = True
            request.session['user_id'] = id[0][0]
            return redirect('admin_home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'admin_login.html')


def admin_home(request):
    id = request.session.get('user_id')
    user = Registration.objects.filter(id=id)
    print(user)
    if request.session.has_key('Is_Login'):
        return render(request, 'admin_index.html',{'user':user})
    return redirect('admin_login')

def admin_banner(request):
    return render(request, 'admin_banner.html')


def admin_show(request, id):
    # email = request.session['email']
    user = Registration.objects.filter(id=id)
    return render(request, 'admin_show_profile.html', {'user': user})


def admin_edit_profile(request, id):
    user = Registration.objects.filter(id=id)
    return render(request, 'admin_edit_profile.html', {'user': user})


def admin_update_profile(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        speciality = request.POST['speciality']

        Registration.objects.filter(id=id).update(name=name, email=email, contact=contact, speciality=speciality)
        messages.success(request,"Profile updated Successfully")

        return redirect('admin_home')


def chnage_password(request):
    id = request.session.get('user_id')
    print(id)
    if request.method == 'POST':
        pw = request.POST['password']
        pwd = hashlib.md5(pw.encode())
        password = pwd.hexdigest()

        cpw = request.POST['conf_password']
        cpwd = hashlib.md5(cpw.encode())
        conf_password = cpwd.hexdigest()

        if password == conf_password:
            Registration.objects.filter(id=id).update(password=password)
            messages.success(request,"Password Updated successfully")
            return redirect('admin_home')
        else:
            messages.error(request, "Password and confirm password should be same")

    return render(request, 'change_password.html')

def get_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        if Registration.objects.filter(email=email):
            request.session['email'] = email
            return redirect('forgot_password')
        else:
            messages.error(request, 'email is incorrect')

    return render(request, 'get_email.html')

def forgot_password(request):
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
            Registration.objects.filter(email=email).update(password=password)
            messages.success(request,"Password Updated successfully")
            return redirect('admin_home')
        else:
            messages.error(request, "Password and confirm password should be same")

    return render(request,'forgot_password.html')


def admin_about_add(request):
    if request.method == 'POST':
        description = request.POST['description']
        img = request.FILES['image']
        obj = About(description=description, image=img)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_about_add.html')


def admin_all_about(request):
    about = About.objects.all()
    return render(request, 'admin_all_about.html', {'about': about})


def admin_about_edit(request, id):
    about = About.objects.get(id=id)
    return render(request, 'admin_about_edit.html', {'about': about})


# obj = About(request.POST,instance=about)
# obj.save()

def admin_about_update(request, id):
    if request.method == 'POST':
        about = get_object_or_404(About, id=id)
        about.image.delete()
        about.delete()
        # update new data
        about.description = request.POST['description']
        about.image = request.FILES['image']
        about.save()
    return redirect('admin_all_about')


def admin_about_delete(request, id):
    about = get_object_or_404(About, id=id)
    if about.image:
        about.image.delete()
    about.delete()
    return redirect('admin_all_about')


def admin_services_add(request):
    if request.method == 'POST':
        service = request.POST['svs_name']
        description = request.POST['description']
        img = request.FILES['image']
        obj = Service(service_name=service, description=description, image=img)
        obj.save()
        messages.success(request, "Data Added")

    return render(request, 'admin_services_add.html')



def admin_services_all(request):
    service = Service.objects.all()
    return render(request, 'admin_all_services.html', {'service': service})


def admin_services_edit(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'admin_service_edit.html', {'service': service})


def admin_services_update(request, id):
    if request.method == 'POST':
        service = get_object_or_404(Service, id=id)
        service.image.delete()
        service.delete()

        service.service_name = request.POST['svs_name']
        service.description = request.POST['description']
        service.image = request.FILES['image']
        service.save()
        return redirect('admin_services_all')


def admin_services_delete(request, id):
    service = get_object_or_404(Service, id=id)
    if service.image:
        service.image.delete()
    service.delete()
    return redirect('admin_services_all')


def admin_reviews_add(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        review = request.POST['review']
        obj = Reviews(firstname=fname, lastname=lname, review=review)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_reviews_add.html')


def admin_reviews_all(request):
    reviews = Reviews.objects.all()
    return render(request, 'admin_reviews_all.html', {'reviews': reviews})


def admin_reviews_edit(request, id):
    reviews = Reviews.objects.get(id=id)
    return render(request, 'admin_reviews_edit.html', {'reviews': reviews})


def admin_reviews_update(request, id):
    if request.method == 'POST':
        reviews = Reviews.objects.get(id=id)

        reviews.firstname = request.POST['fname']
        reviews.lastname = request.POST['lname']
        reviews.review = request.POST['review']
        reviews.save()
        return redirect('admin_reviews_all')


def admin_reviews_delete(request, id):
    reviews = Reviews.objects.get(id=id)
    reviews.delete()
    return redirect('admin_reviews_all')


def admin_team_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        speciality = request.POST['speciality']
        description = request.POST['description']
        obj = Team(name=name, speciality=speciality, description=description)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_team_add.html')


def admin_team_all(request):
    team = Team.objects.all()
    return render(request, 'admin_team_all.html', {'team': team})


def admin_team_edit(request, id):
    team = Team.objects.get(id=id)
    return render(request, 'admin_team_edit.html', {'team': team})


def admin_team_update(request, id):
    if request.method == 'POST':
        team = Team.objects.get(id=id)
        team.name = request.POST['name']
        team.speciality = request.POST['speciality']
        team.description = request.POST['description']
        team.save()
        return redirect('admin_team_all')


def admin_team_delete(request, id):
    team = Team.objects.get(id=id)
    team.delete()
    return redirect('admin_team_all')


def admin_makeup_add(request):
    if request.method == 'POST':
        service = request.POST['service']
        description = request.POST['description']
        obj = Makeup(service=service, description=description)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_makeup_add.html')


def admin_makeup_all(request):
    makeup = Makeup.objects.all()
    return render(request, 'admin_makeup_all.html', {'makeup': makeup})


def admin_makeup_edit(request, id):
    makeup = Makeup.objects.get(id=id)
    return render(request, 'admin_makeup_edit.html', {'makeup': makeup})


def admin_makeup_update(request, id):
    if request.method == 'POST':
        makeup = Makeup.objects.get(id=id)
        makeup.service = request.POST['service']
        makeup.description = request.POST['description']
        makeup.save()
        return redirect('admin_makeup_all')


def admin_makeup_delete(request, id):
    makeup = Makeup.objects.get(id=id)
    makeup.delete()
    return redirect('admin_makeup_all')


def admin_news_add(request):
    if request.method == 'POST':
        header = request.POST['header']
        description = request.POST['description']
        date = request.POST['date']
        image = request.FILES['image']
        obj = LatestNews(news_header=header, news_description=description, image=image, date=date)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_news_add.html')


def admin_news_all(request):
    news = LatestNews.objects.all()
    return render(request, 'admin_news_all.html', {'news': news})


def admin_news_edit(request, id):
    news = LatestNews.objects.get(id=id)
    return render(request, 'admin_news_edit.html', {'news': news})


def admin_news_update(request, id):
    if request.method == 'POST':
        news = get_object_or_404(LatestNews, id=id)
        news.image.delete()
        news.delete()

        news.news_header = request.POST['header']
        news.news_description = request.POST['description']
        news.image = request.FILES['image']
        news.date = request.POST['date']
        news.save()
        return redirect('admin_news_all')


def admin_news_delete(request, id):
    news = LatestNews.objects.get(id=id)
    news.delete()
    return redirect('admin_news_all')


def admin_brand_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        obj = Brands(name=name, image=image)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_brand_add.html')


def admin_brand_all(request):
    brand = Brands.objects.all()
    return render(request, 'admin_brands_all.html', {'brand': brand})


def admin_brand_edit(request, id):
    brand = Brands.objects.get(id=id)
    return render(request, 'admin_brand_edit.html', {'brand': brand})


def admin_brand_update(request, id):
    if request.method == 'POST':
        brand = get_object_or_404(Brands, id=id)
        brand.image.delete()
        brand.delete()

        brand.news_header = request.POST['name']
        brand.image = request.FILES['image']
        brand.save()
        return redirect('admin_brand_all')


def admin_brand_delete(request, id):
    brand = Brands.objects.get(id=id)
    brand.delete()
    return redirect('admin_brand_all')


def admin_blog_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        image = request.FILES['image']
        obj = Blog(title=title, description=description, date=date, image=image)
        obj.save()
        messages.success(request, "Data Added")
    return render(request, 'admin_blog_add.html')


def admin_blog_all(request):
    blog = Blog.objects.all()
    return render(request, 'admin_blog_all.html', {'blog': blog})


def admin_blog_edit(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'admin_blog_edit.html', {'blog': blog})


def admin_blog_update(request, id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=id)
        blog.image.delete()
        blog.delete()

        blog.title = request.POST['title']
        blog.description = request.POST['description']
        blog.date = request.POST['date']
        blog.image = request.FILES['image']
        blog.save()
        return redirect('admin_blog_all')


def admin_blog_delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('admin_blog_all')


def admin_appoinment_all(request):
    appoinment = Appoinment.objects.all
    return render(request, 'admin_appoinment_all.html', {'appoinment': appoinment})

def admin_appoinment_delete(request, id):
    appoinment = Appoinment.objects.get(id=id)
    appoinment.delete()
    return redirect('admin_appoinment_all')

def admin_contact(request):
    contact = Contact.objects.all
    print("Ruk")
    print(contact)
    return render(request,'admin_contact.html',{'contact':contact})

def admin_contact_delete(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('admin_contact')

def admin_logout(request):
    del request.session['Is_Login']
    return redirect('admin_login')


