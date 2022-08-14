from multiprocessing import context
from django.shortcuts import render, HttpResponse

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
    return render(request, "contact.html")