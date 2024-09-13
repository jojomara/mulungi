from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_booking_view, name='book-flight'),
   
]
