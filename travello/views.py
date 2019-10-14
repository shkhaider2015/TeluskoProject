from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Karachi'
    dest1.desc = 'The City That Never Sleep'
    dest1.image = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Peshawar'
    dest2.desc = 'The City of Beuty'
    dest2.image = 'destination_2.jpg'
    dest2.price = 850

    dest3 = Destination()
    dest3.name = 'Islamabad'
    dest3.desc = 'The City of Silence'
    dest3.image = 'destination_3.jpg'
    dest3.price = 600

    dest4 = Destination()
    dest4.name = 'Quetta'
    dest4.desc = 'The City of Desert'
    dest4.image = 'destination_6.jpg'
    dest4.price = 599

    dests = [dest1, dest2, dest3, dest4]

    return render(request, 'index.html', {'dests' : dests})