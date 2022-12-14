from .models import Item,Client,Order
from django.shortcuts import render

def index(request):
    items = Item.objects.all()
    clients = Client.objects.all()
    orders = Order.objects.all()
    return render(request,
                  "store_origin/home_page.html",
                  {'items': items, 'clients': clients, 'orders': orders})


# Create your views here.
