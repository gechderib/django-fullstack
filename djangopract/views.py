from django.http import HttpResponse

def about(request):
    return HttpResponse("about")

def home(request):
    return HttpResponse("Home")