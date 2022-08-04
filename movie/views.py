from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html", {"screenName": "Home"})

def about(request):
    return render(request, "about.html", {"screenName": "About"})