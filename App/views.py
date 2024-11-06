from django.shortcuts import render
from App.models import *
# Create your views here.
def HomePage(request):
  products = Products.objects.all().order_by("-id", "updated_at")
  context={
    'products':products
  }
  return render(request, 'index.html', context)
