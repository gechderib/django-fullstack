from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    # return HttpResponse("About")
    return render(request, "aboutpage.html")

def home(request):
    # return HttpResponse("Home")
    return render(request,"homepage.html")