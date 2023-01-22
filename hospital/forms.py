from django.forms import ModelForm
from django import forms
from .models import Patient,Doctor,Departments,Appointment


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name','patient_dob', 'patient_sex', 'patient_martial', 'patient_number','patient_email', 'patient_height','patient_weight', 'emer_name','emer_contact','emer_relation',  'patient_img','patient_medicationHistory', ]

 

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['doc_name','doc_dob','doc_specialization','doc_experience','doc_age','doc_designation','doc_qualification','doc_depart','doc_phone','doc_gender','doc_Martial','doc_email','doc_address','doc_img']




class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'



class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'