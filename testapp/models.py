from django.db import models

# Create your models here.
class Student(models.Model):
    Id=models.CharField(max_length=4,primary_key=True)
    Name=models.CharField(max_length=30)
    Age=models.CharField(max_length=2)
    GENDER_CHOICES=(
        ('M','M'),
        ('F','F'),
    )
    Gender=models.CharField(max_length=5,choices=GENDER_CHOICES)
    Mob_no=models.BigIntegerField()