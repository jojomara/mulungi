from django.shortcuts import render, redirect
from .forms import FlightBookingForm
from django.contrib import messages


def flight_booking_view(request):
    if request.method == 'POST':
        form = FlightBookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('success')  
    else:
        form = FlightBookingForm()  

    return render(request, 'flight_booking.html', {'form': form})
