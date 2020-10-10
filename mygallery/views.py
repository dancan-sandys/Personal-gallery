from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import Http404, HttpResponse,HttpRequest


# Create your views here.

def gallery(request):

    images = Image.objects.all()
    title = "Gallery"
    return render(request, 'gallery.html', {"images":images, "title":title})

def categories(request):

    categories = Category.objects.all()
    

    return render(request, 'categories.html', {"categories":categories})

def image(request, id):

    try:
        image = Image.objects.get(id =id)
    
    except:
        raise Http404()

    return render(request, 'image.html',{"image": image})


def category(request, id):

    try:
        category = Category.objects.get(id =id)

    except:
        raise Http404()