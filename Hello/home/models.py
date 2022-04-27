from statistics import mode
from django.db import models

# Create your models here.
# makemigrations = create changes and store in a file
#migrate = apply pending changes created by makemigrations


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    passwd = models.CharField(max_length=25)
    date =  models.DateField()

    def __str__(self):
        return self.name
    