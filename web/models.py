from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.user}"

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date =  models.DateTimeField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_date(self):
        return self.date

    def __str__(self):
        return f"{self.text} - {self.amount} on {self.date}"

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_date(self):
        return self.date
    
    def __str__(self):
        return f"{self.text} - {self.amount} on {self.date}"