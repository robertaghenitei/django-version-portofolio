from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "startpage/home.html")

def projects(request):
    return render(request, "startpage/projects.html")

def blog(request):
    return render(request, "startpage/blog.html")

def cv(request):
    return render(request, "startpage/cv.html")

def contact(request):
    return render(request, "startpage/contact.html")

def error_404_view(request, exception):
    return render(request, 'startpage/404.html', status=404)