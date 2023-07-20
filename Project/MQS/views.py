from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, 'home/home.html')

def about (request):
    return render (request, 'about/about.html')

def gallery (request):
    return render (request, 'gallery/gallery.html')

def contact (request):
    return render (request, 'contact/contact.html')