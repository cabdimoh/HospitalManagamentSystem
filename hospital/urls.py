from django.urls import path
from . import views



urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('allPatient/', views.patientall, name='patient_list'),
    path('addpatient/', views.createPatient, name='create_patient'),
    path('P_profile/<str:pk>', views.viewPatient, name='single_patient'),
    path('updatePatient/<str:pk>', views.updatePatient, name='update_patient'),
    path('deletePatient/<str:pk>', views.deletePatient, name='delete_patient'),

    path('Doctors/', views.doctorsList, name='list_doctor'),
    path('CreateDoctor/', views.createDoctor, name='add_doctor'),
    path('updateDoctor/<str:pk>/', views.updateDoctor, name='doctor_update'),
    path('ViewsDoctor/<str:pk>/', views.viewDoctor, name='doctor_view'),
    path('deleteDoctor/<str:pk>/', views.deleteDoctor, name='delete_doctor'),


    path('allDepartment/', views.allDepartments, name='allDepartment'),
    path('CreateDepartment/', views.createDepartment, name='create_Department'),
    path('editDepartment/<str:pk>/', views.editDepartment, name="edit_department"),
    path('delete_Department/<str:pk>/', views.deleteDep, name="delete_department"),




    path('allAppointment/', views.allAppointment, name='allApppointment'),
    path('CreateAppointment/', views.createAppointment, name='create_Appointment'),
    path('editAppointment/<str:pk>/', views.editAppointment, name="edit_Appointment"),
    path('delete_Appointment/<str:pk>/', views.deleteAppointment, name="delete_Appointment"),


]