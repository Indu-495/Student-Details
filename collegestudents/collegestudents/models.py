from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
