from multiprocessing import context
from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from datetime import datetime
from basic_app.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable_1": "This is variable 1",
        "variable_2": "This is variable 2"
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is HOME page")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    return render(request, "contact.html")
