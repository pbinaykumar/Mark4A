from django.db import models

# Create your models here.

class  Contact(models.Model):
    First_Name=models.CharField(max_length=25)
    Last_Name=models.CharField(max_length=25)
    Email_Id = models.CharField(max_length=50)
    Subject=models.CharField(max_length=150)
    def __str__(self):
        return self.First_Name

