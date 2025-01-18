from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Reservation, Customer
from .forms import ReservationForm

def home(request):
    return render(request, 'home.html')

def tables(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html', {'reservations': reservations})

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})

def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'update_reservation.html', {'form': form})

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('reservations')
