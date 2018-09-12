from django.contrib import admin

from .models import *

admin.site.register(Login)
admin.site.register(EmployeeModel)
admin.site.register(Company)
admin.site.register(Supervisor)

# Register your models here.
