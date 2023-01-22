from django.shortcuts import render, redirect
from .models import Patient, Doctor, Departments, Appointment
from .forms import PatientForm, DoctorForm,DepartmentForm,AppointmentForm
from django.contrib.auth.decorators import login_required



# HOME PAGE
@login_required(login_url='login')
def homePage(request):
    return render(request, 'main.html')

# PATIENT PAGES
@login_required(login_url='login')
def createPatient(request):  
    patientlist = Patient.objects.all
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_patient')

    context = {'patientlist': patientlist, 'forms':form }
    return render(request, 'hospital/AddPatient.html', context)

@login_required(login_url='login')
def patientall(request):
    patientlist = Patient.objects.all
    context = {'patientlist': patientlist }
    return render(request, 'hospital/allPatient.html', context)

@login_required(login_url='login')
def viewPatient(request, pk):
    siglePatient = Patient.objects.get(id = pk)
    context = {'singlepatient': siglePatient}
    return render (request, 'hospital/PatientProfile.html', context)

@login_required(login_url='login')
def updatePatient(request, pk):
    pages = 'Patient'
    singleP = Patient.objects.get(id = pk)
    form = PatientForm(instance=singleP)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=singleP)
        if form.is_valid():
            form.save()
            return redirect('create_patient')

    context = { 'formUpdate':form, 'pages':pages }
    return render(request, 'hospital/updateTemplate.html', context)


@login_required(login_url='login')
def deletePatient(request, pk):
    page = 'DeletePatient'
    deletedp = Patient.objects.get(id= pk)
    if request.method == 'POST':
        deletedp.delete()
        return redirect('create_patient')
    context = {'deleteP':deletedp, 'page':page}
    return render(request, 'hospital/deleteTemplate.html', context)

# DOCTOR PAGES
@login_required(login_url='login')
def doctorsList(request):
    doc =  Doctor.objects.all()
    context = {'doctorlist':doc}
    return render(request, 'hospital/Doctors.html', context)


@login_required(login_url='login')
def createDoctor(request):  
    pages = 'Doctor'
    alldoctor = Doctor.objects.all()
    form =  DoctorForm()
    if request.method == "POST": 
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_doctor', )
    context  = {'docform':form ,'alldoctor':alldoctor, 'pages':pages}
    return render(request, 'hospital/AddDoctor.html', context)


@login_required(login_url='login')
def updateDoctor(request, pk):    
    doctorOne = Doctor.objects.get(id = pk)
    formupdate = DoctorForm(instance=doctorOne) 
    if request.method == 'POST':
        formupdate = DoctorForm(request.POST, request.FILES, instance=doctorOne)      
        if formupdate.is_valid():
            formupdate.save()
            return redirect('add_doctor')
    context = { 'formupdate':formupdate}
    return render(request, 'hospital/updateTemplate.html', context)

@login_required(login_url='login')
def viewDoctor(request, pk):
    singleDoctor = Doctor.objects.get(id = pk)
    context = {'singleDoctor': singleDoctor}
    return render(request, 'hospital/DoctorProfile.html', context)

@login_required(login_url='login')
def deleteDoctor(request, pk):
    page = 'deleteDoctor'
    doctorSelf = Doctor.objects.get(id = pk)    
    if request.method == 'POST':
        doctorSelf.delete()
        return redirect('add_doctor')
    context = {'doctorSelf':doctorSelf, 'page':page}
    return render(request, 'hospital/deleteTemplate.html',context)
        


@login_required(login_url='login')
def allDepartments(request):
    allD = Departments.objects.all()
    context = {'allD':allD}
    return render (request, 'hospital/AllDepartMent.html',context)

@login_required(login_url='login')
def createDepartment(request):
    allD = Departments.objects.all()
    dform = DepartmentForm()
    if request.method == "POST":
        dform = DepartmentForm(request.POST, request.FILES)
        if dform.is_valid():
            dform.save()
            return redirect('create_Department')
    context = {'dforms':dform, 'allDs':allD}
    return render(request, 'hospital/createDep.html',context)


@login_required(login_url='login')
def editDepartment(request, pk):
    page = "editDepartment"
    allD = Departments.objects.get(id = pk)
    dform = DepartmentForm(instance=allD)
    if request.method == "POST":
        dform = DepartmentForm(request.POST, request.FILES, instance=allD)
        if dform.is_valid():
            dform.save()
            return redirect('create_Department')
    context = {'dforms':dform, 'page':page}
    return render(request, 'hospital/updateTemplate.html',context)


@login_required(login_url='login')
def deleteDep(request, pk):
    page = 'DeleteDepartment'
    alld = Departments.objects.get(id = pk)
    if request.method == "POST":
        alld.delete()
        return redirect('create_Department')
    context = {'alld':alld, 'page':page}
    return render(request, 'hospital/deleteTemplate.html',context)



#appointment
@login_required(login_url='login')
def allAppointment(request):
    allApp = Appointment.objects.all
    context = {'allapp': allApp}
    return render(request, 'hospital/viewAppointment.html', context)


@login_required(login_url='login')
def createAppointment(request):
    allApp2 = Appointment.objects.all 
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('allApppointment')
    context = {'appforms':form, 'Appoints':allApp2}
    return render(request, 'hospital/BookAppointment.html', context)

@login_required(login_url='login')
def editAppointment(request, pk):
    page = "EditAppointment"
    allApp = Appointment.objects.get(id = pk)
    formapp3 = AppointmentForm(instance=allApp)
    if request.method == 'POST':
        formapp3 = AppointmentForm(request.POST, request.FILES, instance=allApp)
        if formapp3.is_valid:
            formapp3.save()
            return redirect(to='create_Appointment')

    context = {'formApp3':formapp3, 'page':page}
    return render(request, 'hospital/updateTemplate.html',context)



@login_required(login_url='login')
def deleteAppointment(request, pk):
    page  = 'DeleteAppointment'
    allapp4 = Appointment.objects.get(id = pk)
    if request.method == 'POST':
        allapp4.delete()
        return redirect('create_Appointment')
    context = {'allapp4':allapp4, 'page':page}
    return render(request, 'hospital/deleteTemplate.html', context)