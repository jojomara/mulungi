from django.db import models

class FlightBooking(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    po_box = models.CharField(max_length=50, blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=50)
    visa_document = models.FileField(upload_to='visas/', blank=True, null=True)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
