from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tables/', views.tables, name='tables'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/new/', views.make_reservation, name='make_reservation'),
    path('reservations/update/<int:pk>/', views.update_reservation, name='update_reservation'),
    path('reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]
