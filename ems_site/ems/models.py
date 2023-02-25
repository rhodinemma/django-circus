from django.db import models

# Create your models here.


class Employee(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=13, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    dob = models.DateField()
    joining_date = models.DateField()
    jobs = models.ManyToManyField('Job', blank=True)


class Job(models.Model):
    name = models.CharField(max_length=250)