

from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.



def index(request):
    context = {
        'variable' : "this is sent gulugulu",
        'variable2': "this is variable two",
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        passwd = request.POST.get('password')
        contact = Contact(name=name, email=email, phone = phone, passwd=passwd, date = datetime.today())
        contact.save()
        messages.success(request, 'Your form has been saved!!!')
    return render(request, 'contact.html')

