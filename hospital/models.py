from django.db import models
import uuid


class Patient(models.Model):
    CHOSE1 = '.....'
    MALE = 'Male'
    FEMALE = 'Female'
    p_gender = [
        (CHOSE1, '.....'),
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    CHOSE2 = '.....'
    MARRIED = "MARRIED"
    SINGLE = "SINGLE"
    DIVERCED = "DIVERCED"
    
    p_Martial = [
        (CHOSE2, '......'),
        (MARRIED, 'MARRIED'),
        (SINGLE, 'SINGLE'),
        (DIVERCED, 'DIVERCED'),
    ]
    patient_name = models.CharField(max_length=60)
    patient_dob = models.DateField()
    patient_sex = models.CharField(max_length=20, choices=p_gender, default=CHOSE1)
    patient_martial = models.CharField(max_length=20, choices=p_Martial, default=CHOSE2)
    patient_number = models.IntegerField(help_text='patient phone number')
    patient_email = models.EmailField()
    patient_height = models.FloatField(blank=True, null=True)
    patient_weight = models.FloatField(blank=True, null=True)
    patient_medicationHistory =models.TextField(blank=True, null=True)
    emer_name = models.CharField(max_length=200, blank=True, null=True)
    patient_img = models.ImageField(blank=True, null=True, default='images/default.jpg')
    emer_contact = models.IntegerField(default=1)
    emer_relation = models.CharField(max_length=200, blank=True, null=True)
    created  = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default= uuid.uuid4,unique=True, primary_key = True, editable= False )

    

    def __str__(self):
        return self.patient_name



class Doctor(models.Model):
    CHOSE1 = '.....'
    MALE = 'Male'
    FEMALE = 'Female'
    d_gender  = [
        (CHOSE1, '.....'),
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]

    CHOSE2 = '.....'
    MARRIED = "MARRIED"
    SINGLE = "SINGLE"
    DIVERCED = "DIVERCED"
    
    d_marital  = [
        (CHOSE2, '......'),
        (MARRIED, 'MARRIED'),
        (SINGLE, 'SINGLE'),
        (DIVERCED, 'DIVERCED'),
    ]
    doc_name = models.CharField(max_length=200)
    doc_dob = models.DateField()
    doc_specialization = models.CharField(max_length=200,blank=True, null=True)
    doc_experience = models.CharField(max_length=200, blank=True, null=True)
    doc_age = models.IntegerField()
    doc_designation = models.CharField(max_length=200, )
    doc_qualification = models.CharField(max_length=200, )
    doc_depart = models.CharField(max_length=200)
    doc_phone = models.IntegerField()
    doc_gender = models.CharField(max_length=10, choices=d_gender ,default= CHOSE1)
    doc_Martial = models.CharField(max_length=10, choices=d_marital , default= CHOSE2)
    doc_email = models.EmailField()
    doc_address = models.CharField(max_length=300, blank=True, null=True)
    doc_img = models.ImageField(blank=True, null=True, default='images/doctorimg.png')
    created  = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default= uuid.uuid4,unique=True, primary_key = True, editable= False ) 
  
    def __str__(self):
        return self.doc_name
        
class Appointment(models.Model):   
    Doct_name =models.CharField(max_length=200, blank=True, null=True)
    opdate = models.DateField(blank=True, null=True)
    time_slot = models.TimeField(blank=True, null=True)
    p_problem = models.TextField(blank=True, null=True)
    tokenNum = models.IntegerField(blank=True, null=True)
    created  = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default= uuid.uuid4,unique=True, primary_key = True, editable= False )

    def __str__(self):
        return self.Doct_name



class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_head = models.CharField(max_length=100)
    dep_location = models.CharField(max_length=100)
    dep_phone  = models.PositiveBigIntegerField()
    created  = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default= uuid.uuid4,unique=True, primary_key = True, editable= False )
   

    def __str__(self):
        return self.dep_name 