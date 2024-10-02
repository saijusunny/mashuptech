from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    complete = models.BooleanField(default=True)

class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    task_assign =models.TextField()
    complete = models.BooleanField(default=False)