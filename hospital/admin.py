from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor,Appointment, Departments

# Register your models here.


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Departments)
