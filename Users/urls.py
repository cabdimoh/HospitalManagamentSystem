from django.urls import path
from . import views


urlpatterns = [
    path('login_page/', views.login_User, name='login'),
    path('logout_page/', views.logout_user, name='logout'),
]