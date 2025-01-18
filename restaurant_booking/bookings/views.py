from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Table, Reservation, Customer

def home(request):
    return render(request, 'home.html')

def tables(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def reservations(request):
    reservations = Reservation.objects.select_related('customer', 'table').all()
    return render(request, 'reservation.html', {'reservations': reservations})

def book_table(request):
    if request.method == "POST":
        customer_name = request.POST.get('name')
        customer_email = request.POST.get('email')
        table_id = request.POST.get('table_id')
        date = request.POST.get('date')
        time = request.POST.get('time')

        customer, created = Customer.objects.get_or_create(name=customer_name, email=customer_email)
        table = get_object_or_404(Table, id=table_id, is_available=True)

        Reservation.objects.create(customer=customer, table=table, date=date, time=time)
        table.is_available = False
        table.save()

        return JsonResponse({"message": "Reservation created successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)
