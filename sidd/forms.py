from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 200, widget = forms.PasswordInput())

class EmployeeDetails(forms.Form):
    email = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 200, widget = forms.PasswordInput())
    name = forms.CharField(max_length = 100)
    age = forms.CharField(max_length = 100)
    ctc = forms.CharField(max_length = 100)
    project = forms.CharField(max_length = 100)
    
class CompanyForm(forms.Form):
    companyname = forms.CharField(max_length = 100)
    companyaddress = forms.CharField(max_length = 100)
    companybusiness = forms.CharField(max_length = 100)

class Supervisor(forms.Form):
    supervisorname = forms.CharField(max_length = 100)
    supervisorcompanyid = forms.CharField(max_length = 100)
    supervisorusername = forms.CharField(max_length = 100)
    supervisorpassword = forms.CharField(max_length = 100)