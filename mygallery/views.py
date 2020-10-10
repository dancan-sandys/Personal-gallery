from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import Http404, HttpResponse,HttpRequest


# Create your views here.

def gallery(request):

    images = Image.objects.all()
    title = "Gallery"
    return render(request, 'gallery.html', {"images":images, "title":title})

