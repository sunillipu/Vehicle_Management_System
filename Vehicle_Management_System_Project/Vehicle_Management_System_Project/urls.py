"""Vehicle_Management_System_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Vehicle_Management_System_Application import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_view),
    url(r'^super_admin_login/',views.super_admin_login_view),
    url(r'^super_admin_registration/',views.super_admin_registration_view),
    url(r'^create/',views.create_view),
    url(r'^retrive/',views.retrive_view),
    url(r'^update/',views.update_view),
    url(r'^delete/',views.delete_view),
    url(r'^admin_login/',views.admin_login_view),
    url(r'^admin_registration/',views.admin_registration_view),
    url(r'^user_login/',views.user_login_view),
    url(r'^user_registration/',views.user_registration_view)



]
