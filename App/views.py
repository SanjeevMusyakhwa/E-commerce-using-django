from django.shortcuts import render
from App.models import *
# Create your views here.
def HomePage(request):
  # products = Products.objects.all().order_by("-id", "updated_at")
  products = Products.objects.filter(featured= True, product_status ='published')
  context={
    'products':products
  }
  return render(request, 'index.html', context)


def Product_list_view(request):
  products = Products.objects.filter(product_status ='published')
  context={
    'products':products
  }
  return render(request, 'Products/product_list.html', context)



def Category_list_view(request):
  categories = Category.objects.all()
  context = {
    'categories': categories
  }
  return render(request,'Category/category_list.html', context)