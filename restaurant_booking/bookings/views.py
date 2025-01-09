from django.shortcuts import render
from .models import Table, Reservation

def home(request):
    return render(request, 'home.html')

def tables(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})
