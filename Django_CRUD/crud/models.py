from django.db import models

# Create your models here.

class ParcelList(models.Model):
    tracking_no = models.CharField(max_length=150)
    postcode = models.IntegerField()
    address = models.CharField(max_length=100)
    #id = models.CharField(max_length=50,primary_key=True)
    compartment = models.IntegerField(default=0)
    destination = models.CharField(max_length=100,default='undefined')
    def __str__(self):
        return self.tracking_no

class DriverList(models.Model):
    zone = models.CharField(max_length=100)
    min_postcode = models.IntegerField()
    max_postcode = models.IntegerField()
    compartment = models.IntegerField()
    #id = models.CharField(max_length=50,primary_key=True)


    def __str__(self):
        return self.zone
