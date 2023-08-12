from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    mob_no=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(max_length=150)
