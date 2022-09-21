from django.db import models

class Employees(models.Model):
    name= models.CharField(max_length=200, blank=False, null=True )
    email=models.EmailField(max_length=100, blank=False, null=True)
    address=models.TextField(blank=False,  null=True)
    phone=models.IntegerField(blank=False,  null=True) 
    def __str__(self):
        return self.name