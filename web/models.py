from django.db import models
from django.contrib.auth.models import User
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date =  models.DateTimeField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)