from django.db import models

# Create your models here.
gen = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class Patient(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, choices=gen)
    age = models.IntegerField()
    disease_Problem = models.TextField(max_length=500)
    doctor_name = models.CharField(max_length=40)
    doctor_fees = models.IntegerField(default=500)
    started_meds_on_date = models.DateField()
