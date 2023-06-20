from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=12)
    email = models.CharField(max_length=12)
    room = models.CharField(max_length=12)
    guests = models.CharField(max_length=20)
    arrival = models.DateField()
    departure = models.DateField()
    special = models.TextField()

    def __str__(self):
        return self.name
