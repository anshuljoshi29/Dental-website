from email import message
import email
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import appoints
import os
from dotenv import load_dotenv
load_dotenv()
# Create your views here.views takes request ,give response or render

#home page view
def home(request):
    if request.method =="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        schedule=request.POST.get('schedule')
        day=request.POST.get('day')
        message=request.POST.get('message')
        obj=appoints()
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.address=address
        obj.schedule=schedule
        obj.day=day
        obj.message=message
        obj.save()
        return render(request,'home.html',{})
    
    else:
        return render(request,'home.html',{})


#contact page view
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        send_mail(
            name,
            message,
            email,
            ['deathgod2908@gmail.com']
            )
        return render(request,'contact.html', {'name':name})
    
    else:
        return render(request,'contact.html',{})

#pricing page view
def pricing(request):
    return render(request,"pricing.html",{})

#about page view
def about(request):
    return render(request,"about.html",{})

#service page view
def service(request):
    return render(request,'service.html',{})

#blog page view
def blog(request):
    return render(request,'blog.html',{})

#blog detail page view
def blog_details(request):
    return render(request,'blog-details.html',{})

#table page view
def table(request):
    if request.method=="POST":
        data=appoints.objects.all()
        return render(request,'table.html',{'data':data})

#panel page view
def panel(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=appoints.objects.all()
        if email==os.getenv("user_name") and password==os.getenv("user_pass"):
            return render(request,'table.html',{'data':data})
        else:
            return render(request,'panel.html',{})
    else:
        return render(request,'panel.html',{})

def delete_event(request , id):
    appoints.objects.filter(id=id).delete()
    return render(request, 'table.html',{})