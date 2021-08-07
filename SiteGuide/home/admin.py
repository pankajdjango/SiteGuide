from django.contrib import admin
from . models import Patient
# Register your models here.
class Show_Admin_Data(admin.ModelAdmin):
    list_display = ['first_name','last_name','gender','age','disease_Problem','doctor_name','doctor_fees','started_meds_on_date']
admin.site.register(Patient,Show_Admin_Data)
