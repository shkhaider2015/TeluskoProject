from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Karachi'
    dest1.desc = 'The City That Never Sleep'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Peshawar'
    dest2.desc = 'The City of Beuty'
    dest2.price = 850

    dest3 = Destination()
    dest3.name = 'Islamabad'
    dest3.desc = 'The City of Silence'
    dest3.price = 600

    return render(request, 'index.html', {'obj' : dest1, 'obj2' : dest2, 'obj3' : dest3})