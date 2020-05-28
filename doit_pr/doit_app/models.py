from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=400,unique=True)
    status = models.BooleanField(default=True)
    task_age = models.CharField(max_length=10,default="All")

class Player(models.Model):
    name = models.CharField(max_length=200)
    age= models.IntegerField(default = 10)
