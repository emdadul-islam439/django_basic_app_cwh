from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is HOME page")
def about(request):
    return HttpResponse("This is ABOUT page")
def services(request):
    return HttpResponse("This is SERVICES page")
def contact(request):
    return HttpResponse("This is CONTACT page")