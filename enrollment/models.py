from datetime import date

from django.db import models

# Create your models here.
class Student(models.Model):
    # TODO: Add first_name/last_name and dynamic searching on either
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(default=date.today)

class StudentToCourse(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)