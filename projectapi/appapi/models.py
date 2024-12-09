from django.db import models


# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    interests = models.CharField(max_length=200)
    gpa = models.FloatField()

    def __str__(self):
        return self.fullname