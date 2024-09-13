from django.contrib import admin
from .models import FlightBooking

@admin.register(FlightBooking)
class FlightBookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'departure_city', 'destination_city')

