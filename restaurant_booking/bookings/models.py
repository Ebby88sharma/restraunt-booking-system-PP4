from django.db import models
from django.core.exceptions import ValidationError

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        overlapping_reservations = Reservation.objects.filter(
            table=self.table,
            date=self.date,
            time=self.time
        )
        if overlapping_reservations.exists():
            raise ValidationError(f"Table {self.table.number} is already booked for this time.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation by {self.customer.name} on {self.date} at {self.time}"
