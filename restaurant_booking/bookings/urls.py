from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tables/', views.tables, name='tables'),
    path('reservations/', views.reservations, name='reservations'),
    path('book/', views.book_table, name='book_table'),
]
