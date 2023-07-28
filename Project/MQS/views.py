from django.shortcuts import render, HttpResponse, redirect

from . models import Input

# Create your views here.

def home (request):
    return render(request, 'home/home.html', {'navbar': 'home'})

def about (request):
    return render(request, 'about/about.html', {'navbar': 'about'})

def gallery (request):
    return render(request, 'gallery/gallery.html', {'navbar': 'gallery'})

def contact (request):

    y = Input.objects.all()


    return render(request, 'contact/contact.html',{"y": y, 'navbar':'contact'})

def details (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')



        data = Input(name=name, email=email, subject=subject)
        data.save()

        return redirect("/contact")


    return HttpResponse("Well received, Thankyou!")