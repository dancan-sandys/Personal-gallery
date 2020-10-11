from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import Http404, HttpResponse,HttpRequest
import pyperclip

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
        images = Image.objects.get(category=category)
    except:
        raise Http404()

    return render(request,'category.html', {"category": category})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category").capitalize()
        category_searched = Category.objects.get(name = search_term)
        images = Image.objects.filter(category=category_searched)
        message = f"{search_term}"

        return render(request, "search.html", {"message":message, "category": category_searched, "images":images})

    else:
        message = "the category you entered is not available"

        return render(request, "search.html", {"message":message})

def image_locations(request):

    images = Image.objects.all()

    return render(request, "locations.html", {"images":images})


def copy(request, id):

    image = Image.objects.get(id = id)
    image_url = image.image_url
    pyperclip.copy(image_url)

