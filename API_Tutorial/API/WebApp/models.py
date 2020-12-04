from django.db import models
from phone_field import PhoneField

# Create your models here.
class Employee(models.Model):
    Email=models.EmailField(max_length=100)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10)
    Profession=models.CharField(max_length=50)
    Role=models.CharField(max_length=50)
    Contact = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.FirstName