from django.db import models

class Login(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class EmployeeModel(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
   
    name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
   
    ctc = models.CharField(max_length = 100)
    project = models.CharField(max_length = 100)

class Company(models.Model):
    companyname = models.CharField(max_length = 100)
    companyaddress = models.CharField(max_length = 100)
    companybusiness = models.CharField(max_length = 100)

class Supervisor(models.Model):
    supervisorname = models.CharField(max_length = 100)
    supervisorcompanyid = models.CharField(max_length = 100)
    supervisorusername = models.CharField(max_length = 100)
    supervisorpassword = models.CharField(max_length = 100)
	
# Create your models here.
