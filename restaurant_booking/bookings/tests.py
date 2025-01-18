from django.test import TestCase
from .models import Table, Customer, Reservation

class ModelsTestCase(TestCase):
    def setUp(self):
        self.table = Table.objects.create(number=1, capacity=4)
        self.customer = Customer.objects.create(name="John Doe", email="john@example.com")
        self.reservation = Reservation.objects.create(
            customer=self.customer, table=self.table, date="2025-01-01", time="18:00:00"
        )

    def test_table_creation(self):
        self.assertEqual(str(self.table), "Table 1 (Capacity: 4)")

    def test_customer_creation(self):
        self.assertEqual(str(self.customer), "John Doe")

    def test_reservation_creation(self):
        self.assertEqual(
            str(self.reservation),
            "Reservation by John Doe on 2025-01-01 at 18:00:00"
        )
