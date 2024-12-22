from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Patient(User):
    age = models.IntegerField()
    goal = models.TextField()

class Doctor(User):
    age_range = models.CharField(max_length=50)
