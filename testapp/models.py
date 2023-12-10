import base64
from django.db import models

class AddressDetails(models.Model):
    hno = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class WorkExperience(models.Model):
    companyName = models.CharField(max_length=255)
    fromDate = models.DateField()
    toDate = models.DateField()
    address = models.CharField(max_length=255)

class Qualification(models.Model):
    qualificationName = models.CharField(max_length=255)
    fromDate = models.DateField()
    toDate = models.DateField()
    percentage = models.FloatField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=15, blank=True, null=True)
    addressDetails = models.OneToOneField(AddressDetails, on_delete=models.CASCADE)
    photo_base64 = models.TextField(blank=True, null=True)
    workExperience = models.OneToOneField(WorkExperience, on_delete=models.CASCADE)
    qualifications = models.OneToOneField(Qualification, on_delete=models.CASCADE)
    projects = models.OneToOneField(Project, on_delete=models.CASCADE)

    @property
    def photo_data_uri(self):
        if self.photo_base64:
            return f'data:image/png;base64,{self.photo_base64}'

    def save_base64_photo(self, base64_data):
        if base64_data:
            self.photo_base64 = base64_data.split(',')[1]

    def save(self, *args, **kwargs):
        # If you want to save the actual image file as well, you can handle it here.
        super().save(*args, **kwargs)
