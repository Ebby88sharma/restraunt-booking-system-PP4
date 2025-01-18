from django.contrib import admin
from .models import Table, Customer, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('number',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date', 'time', 'created_at')
    list_filter = ('date', 'table')
    search_fields = ('customer__name', 'table__number')
