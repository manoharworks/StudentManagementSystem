from django.db import models


class Student(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1,blank=True, null=True, choices= GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="students/", blank=True, null=True)

    def __str__(self):
        return self.name