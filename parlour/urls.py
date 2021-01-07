"""parlour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminservice import views as adminsvs
from userservices import views as usersvs
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',usersvs.home,name="home"),
    path('about',usersvs.about,name="about"),
    path('services',usersvs.services,name="services"),
    path('blog',usersvs.blog,name="blog"),
    path('contact',usersvs.contact,name="contact"),
    path('service_page', usersvs.service_page, name="service_page"),
    path('appoinment', usersvs.appoinment, name="appoinment"),
    path('login', usersvs.login, name="login"),
    path('register', usersvs.register, name="register"),
    path('sidebar/<int:id>', usersvs.sidebar, name="sidebar"),
    path('show_profile', usersvs.show_profile, name="show_profile"),
    path('editProfile', usersvs.editProfile, name="editProfile"),
    path('updateProfile', usersvs.updateProfile, name="updateProfile"),
    path('changePassword', usersvs.changePassword, name="changePassword"),
    path('user_get_email', usersvs.user_get_email, name="user_get_email"),
    path('user_forgot_password', usersvs.user_forgot_password, name="user_forgot_password"),
    path('signout', usersvs.signout, name="signout"),
    #admin
    path('admin_login', adminsvs.admin_login, name="admin_login"),
    path('admin_register', adminsvs.admin_register, name="admin_register"),
    path('admin_home', adminsvs.admin_home, name="admin_home"),
    path('admin_show/<int:id>', adminsvs.admin_show, name="admin_show"),
    path('admin_show/admin_edit_profile/<int:id>', adminsvs.admin_edit_profile, name="admin_edit_profile"),
    path('admin_show/admin_edit_profile/admin_update_profile/<int:id>', adminsvs.admin_update_profile, name="admin_update_profile"),
    path('chnage_password', adminsvs.chnage_password, name="chnage_password"),
    path('get_email', adminsvs.get_email, name="get_email"),
    path('forgot_password', adminsvs.forgot_password, name="forgot_password"),

    # About
    path('admin_about_add', adminsvs.admin_about_add, name="admin_about_add"),
    path('admin_all_about', adminsvs.admin_all_about, name="admin_all_about"),
    path('admin_about_edit/<int:id>', adminsvs.admin_about_edit, name="admin_about_edit"),
    path('admin_about_update/<int:id>', adminsvs.admin_about_update, name="admin_about_update"),
    path('admin_about_delete/<int:id>', adminsvs.admin_about_delete, name="admin_about_delete"),
    #services
    path('admin_services_add',adminsvs.admin_services_add,name="admin_services_add"),
    path('admin_services_all',adminsvs.admin_services_all,name="admin_services_all"),
    path('admin_services_edit/<int:id>',adminsvs.admin_services_edit,name="admin_services_edit"),
    path('admin_services_update/<int:id>',adminsvs.admin_services_update,name="admin_services_update"),
    path('admin_services_delete/<int:id>',adminsvs.admin_services_delete,name="admin_services_delete"),
    #reviews
    path('admin_reviews_add', adminsvs.admin_reviews_add, name="admin_reviews_add"),
    path('admin_reviews_all', adminsvs.admin_reviews_all, name="admin_reviews_all"),
    path('admin_reviews_edit/<int:id>', adminsvs.admin_reviews_edit, name="admin_reviews_edit"),
    path('admin_reviews_update/<int:id>', adminsvs.admin_reviews_update, name="admin_reviews_update"),
    path('admin_reviews_delete/<int:id>', adminsvs.admin_reviews_delete, name="admin_reviews_delete"),
    #team
    path('admin_team_add', adminsvs.admin_team_add, name="admin_team_add"),
    path('admin_team_all', adminsvs.admin_team_all, name="admin_team_all"),
    path('admin_team_edit/<int:id>', adminsvs.admin_team_edit, name="admin_team_edit"),
    path('admin_team_update/<int:id>', adminsvs.admin_team_update, name="admin_team_update"),
    path('admin_team_delete/<int:id>', adminsvs.admin_team_delete, name="admin_team_delete"),
    #makeup
    path('admin_makeup_add', adminsvs.admin_makeup_add, name="admin_makeup_add"),
    path('admin_makeup_all', adminsvs.admin_makeup_all, name="admin_makeup_all"),
    path('admin_makeup_edit/<int:id>', adminsvs.admin_makeup_edit, name="admin_makeup_edit"),
    path('admin_makeup_update/<int:id>', adminsvs.admin_makeup_update, name="admin_makeup_update"),
    path('admin_makeup_delete/<int:id>', adminsvs.admin_makeup_delete, name="admin_makeup_delete"),
    #news
    path('admin_news_add', adminsvs.admin_news_add, name="admin_news_add"),
    path('admin_news_all', adminsvs.admin_news_all, name="admin_news_all"),
    path('admin_news_edit/<int:id>', adminsvs.admin_news_edit, name="admin_news_edit"),
    path('admin_news_update/<int:id>', adminsvs.admin_news_update, name="admin_news_update"),
    path('admin_news_delete/<int:id>', adminsvs.admin_news_delete, name="admin_news_delete"),
    #brands
    path('admin_brand_add', adminsvs.admin_brand_add, name="admin_brand_add"),
    path('admin_brand_all', adminsvs.admin_brand_all, name="admin_brand_all"),
    path('admin_brand_edit/<int:id>', adminsvs.admin_brand_edit, name="admin_brand_edit"),
    path('admin_brand_update/<int:id>', adminsvs.admin_brand_update, name="admin_brand_update"),
    path('admin_brand_delete/<int:id>', adminsvs.admin_brand_delete, name="admin_brand_delete"),
    #brands
    path('admin_blog_add', adminsvs.admin_blog_add, name="admin_blog_add"),
    path('admin_blog_all', adminsvs.admin_blog_all, name="admin_blog_all"),
    path('admin_blog_edit/<int:id>', adminsvs.admin_blog_edit, name="admin_blog_edit"),
    path('admin_blog_update/<int:id>', adminsvs.admin_blog_update, name="admin_blog_update"),
    path('admin_blog_delete/<int:id>', adminsvs.admin_blog_delete, name="admin_blog_delete"),
    #appoinment
    path('admin_appoinment_all', adminsvs.admin_appoinment_all, name="admin_appoinment_all"),
    path('admin_appoinment_delete/<int:id>', adminsvs.admin_appoinment_delete, name="admin_appoinment_delete"),
    #contact
    path('admin_contact', adminsvs.admin_contact, name="admin_contact"),
    path('admin_contact_delete/<int:id>', adminsvs.admin_contact_delete, name="admin_contact_delete"),
    #logout
    path('admin_logout', adminsvs.admin_logout, name="admin_logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
