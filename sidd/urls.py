from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView,EmployeeView,CompanyView,ProfessView
from . import urls
urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('company/', CompanyView.as_view(), name='company'),
    path('profess/', ProfessView.as_view(), name='profess'),
   
]