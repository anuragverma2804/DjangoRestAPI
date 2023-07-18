from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Company(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    type=models.CharField(choices=[("Finance", "Finance"),("IT","IT")],max_length=20)


    objects=models.Manager()

    def __str__(self):
        if self.id==None:
            return "No Company Added"
        else:
            return self.name

class Employee(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    company=models.OneToOneField(Company,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)

    objects=models.Manager()

    def __str__(self):
        if self.id==None:
            return "No Employee Added"
        else:
            return self.name




