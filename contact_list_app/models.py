from django.db import models

class Contact(models.Model):
    Full_Name = models.CharField(max_length=200)
    Relationship = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Phone_No = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)

    def  __str__(self):
        return self.Full_Name
