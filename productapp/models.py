from django.db import models

class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=20,decimal_places=2)
    pmfd=models.DateField()

# Create your models here.
