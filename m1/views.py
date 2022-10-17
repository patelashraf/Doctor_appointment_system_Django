from datetime import date, datetime
import imp
from turtle import title
from django.shortcuts import render, HttpResponse  

from requests import Request
from m1.models import Contact
from authenticate_me.models import dr_reg
from django.contrib import messages
# Create your views here.

def home(request):
    dr_data = dr_reg.objects.all()
    data ={
        'dr_data':dr_data
    }
    return render(request, 'home.html',data)  
    

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,message=message,date=date.today())
        contact.save()
        messages.success(request, 'Soon We,ll contact you')
        return render(request, 'contactus.html', {'name':name})
    else:
        return render(request, 'contactus.html')

def about(request):
    return render(request, 'aboutus.html')

def search(request):
    query = request.GET['query']
    alldata = dr_reg.objects.filter(specialisation__contains=query)
    params = {'alldata': alldata}
    return render(request,'searchfile.html',params)
    