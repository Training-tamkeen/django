from django.shortcuts import render
# from django.http import HttpResponse  //Great for shortcut html

# Create your views here.
from .models import Product

from .forms import ProductCreateForm

def home_view(request, *args, **kwargs):
    context = {
        "my_text": "This is home page, yeahh!!!",
        "list": [1,2,3,4,5,6,7,8,9]
    }
    return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def single_product_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'product': obj
    }
    return render(request, 'product/detail.html', context)

def single_product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request, 'product/create.html', context)