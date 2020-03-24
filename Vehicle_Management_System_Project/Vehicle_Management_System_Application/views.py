from django.shortcuts import render,redirect
from .models import *
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import *
def home_view(request):
    return render(request,'home.html')

# def super_admin_registration_view(request):
#     context={}
#     if request.method=='POST':
#         lform=Super_Admin_Login_Form(request.POST)
#         if lform.is_valid():
#             username=request.POST.get('username','')
#             password=request.POST.get('password','')
#             user = User.objects.create_user(username,password )
#             # uname=Super_Admin_Data.objects.filter(super_admin_user_name=username)
#             # pwd=Super_Admin_Data.objects.filter(super_admin_password=password)
#             # user=auth.authenticate(username=username,password=password)
#             #
#             #
#             # if uname and pwd :
#             #     return HttpResponse('Login Successfully..........')
#             # else:
#             #     return HttpResponse('Invalid Data....')
#             if user:
#                 login(request,user)
#                 return render(request,'crud.html')
#             else:
#                 context["error"] = "Provide valid credentials"
#                 return render(request, 'super_admin_registration.html', context)
#         else:
#             context["error"] = "Provide valid credentials"
#     else:
#         lform=Super_Admin_Login_Form()
#         return render(request,'super_admin_login.html',{'lform':lform})

#
# def super_admin_login_view(request):
#     context = {}
#     if request.method=='POST':
#         lform=Super_Admin_Login_Form(request.POST)
#         if lform.is_valid():
#             name_r = request.POST.get('username','')
#             password_r = request.POST.get('password','')
#             username=name_r
#             password=password_r
#             user = authenticate(request, username=name_r, password=password_r)
#             if user:
#                 login(request, user)
#             # username = request.session['username']
#                 context["user"] = name_r
#                 context["id"] = request.user.id
#                 return render(request, 'crud.html', context)
#             # return HttpResponseRedirect('success')
#         else:
#             context["error"] = "Provide valid credentials"
#             return render(request, 'super_admin_login.html', context)
#             # username=request.POST.get('username','')
#             # password=request.POST.get('password','')
#             # uname=Super_Admin_Data.objects.filter(super_admin_user_name=username)
#             # pwd=Super_Admin_Data.objects.filter(super_admin_password=password)
#             # if uname and pwd :
#             #     return render(request,"crud.html")
#             # else:
#             #     return HttpResponse('Invalid Data....')
#         # else:
#         #     return HttpResponse('Invalid Form')
#     else:
#         lform=Super_Admin_Login_Form()
#         return render(request,'super_admin_login.html',{'lform':lform})
#
#

def super_admin_login_view(request):
    if request.method=='POST':
        lform=Super_Admin_Login_Form(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            uname=Super_Admin_Data.objects.filter(super_admin_user_name=username)
            pwd=Super_Admin_Data.objects.filter(super_admin_password=password)
            if uname and pwd :
                return render(request,"crud.html")
            else:
                return HttpResponse('Invalid Data....')
        else:
            return HttpResponse('Invalid Form')
    else:
        lform=Super_Admin_Login_Form()
        return render(request,'super_admin_login.html',{'lform':lform})
def super_admin_registration_view(request):
    if request.method == 'POST':
        rform=Super_Admin_Registration_Form(request.POST)
        if rform.is_valid():
            name=rform.cleaned_data.get('name','')
            username = rform.cleaned_data.get('username','')
            password = rform.cleaned_data.get('password','')
            data=Super_Admin_Data(
                name=name,
                super_admin_user_name=username,
                super_admin_password=password
            )
            data.save()
            return redirect(super_admin_login_view)
            # Super_Admin_Login_Form=Super_Admin_Login_Form()
            # return render(request,'super_admin_login.html',{'lform':Super_Admin_Login_Form})
        else:
            return HttpResponse('invalid Data...')
    else:
        rform=Super_Admin_Registration_Form()
        return render(request,'super_admin_registration.html',{'rform':rform})

def create_view(request):
    if request.method =="POST":
        vehicle_number=request.POST.get('vehicle_number','')
        vehicle_type=request.POST.get('vehicle_type','')
        vehicle_model=request.POST.get('vehicle_model','')
        vehicle_description=request.POST.get('vehicle_description','')
        data=Vehicle_Details(
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            vehicle_model=vehicle_model,
            vehicle_description=vehicle_description)
        data.save()
        return render(request,'create.html')
    return render(request,'create.html')
def retrive_view(request):
    vehicle_data=Vehicle_Details.objects.all()
    return render(request,'retrive.html',{'vdata':vehicle_data})
def update_view(request):
    if request.method=="POST":
        vehicle_number=request.POST.get('vehicle_number','')
        vehicle_type=request.POST.get('vehicle_type','')
        vehicle_model=request.POST.get('vehicle_model','')
        vehicle_description=request.POST.get('vehicle_description','')
        v_number=Vehicle_Details.objects.filter(vehicle_number=vehicle_number)
        if not v_number:
            return HttpResponse("Vehicle Number is Not Available")
        else:
            v_number.update(
                vehicle_type=vehicle_type,
                vehicle_model=vehicle_model,
                vehicle_description=vehicle_description)
            return render(request,'update.html')
    else:
        return render(request,'update.html')

def delete_view(request):
    if request.method=="POST":
        vehicle_number=request.POST.get('vehicle_number','')
        v_number=Vehicle_Details.objects.filter(vehicle_number=vehicle_number)
        if not v_number:
            return HttpResponse("Vehicle Number is Not Available")
        else:
            v_number.delete()
            return render(request,'delete.html')
    return render(request,'delete.html')
def admin_login_view(request):
    if request.method=='POST':
        lform=Admin_Login_Form(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            uname=Admin_Data.objects.filter(admin_user_name=username)
            pwd=Admin_Data.objects.filter(admin_password=password)
            if uname and pwd :
                return render(request,"admin_home.html")
            else:
                return HttpResponse('Invalid Data....')
        else:
            return HttpResponse('Invalid Form')
    else:
        lform=Admin_Login_Form()
        return render(request,'admin_login.html',{'lform':lform})
def admin_registration_view(request):
    if request.method == 'POST':
        rform=Admin_Registration_Form(request.POST)
        if rform.is_valid():
            name=rform.cleaned_data.get('name','')
            username = rform.cleaned_data.get('username','')
            password = rform.cleaned_data.get('password','')
            data=Admin_Data(
                name=name,
                admin_user_name=username,
                admin_password=password
            )
            data.save()
            return redirect(admin_login_view)
            # Super_Admin_Login_Form=Super_Admin_Login_Form()
            # return render(request,'super_admin_login.html',{'lform':Super_Admin_Login_Form})
        else:
            return HttpResponse('invalid Data...')
    else:
        rform=Admin_Registration_Form()
        return render(request,'admin_registration.html',{'rform':rform})
def user_login_view(request):
    vehicle_data=Vehicle_Details.objects.all()
    if request.method=='POST':
        lform=User_Login_Form(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            uname=User_Data.objects.filter(user_name=username)
            pwd=User_Data.objects.filter(user_password=password)
            if uname and pwd :
                return render(request,"user_home.html",{'vdata':vehicle_data})
            else:
                return HttpResponse('Invalid Data....')
        else:
            return HttpResponse('Invalid Form')
    else:
        lform=User_Login_Form()
        return render(request,'user_login.html',{'lform':lform})
def user_registration_view(request):
    if request.method == 'POST':
        rform=User_Registration_Form(request.POST)
        if rform.is_valid():
            name=rform.cleaned_data.get('name','')
            username = rform.cleaned_data.get('username','')
            password = rform.cleaned_data.get('password','')
            data=User_Data(
                name=name,
                user_name=username,
                user_password=password
            )
            data.save()
            return redirect(user_login_view)
            # Super_Admin_Login_Form=Super_Admin_Login_Form()
            # return render(request,'super_admin_login.html',{'lform':Super_Admin_Login_Form})
        else:
            return HttpResponse('invalid Data...')
    else:
        rform=User_Registration_Form()
        return render(request,'user_registration.html',{'rform':rform})
