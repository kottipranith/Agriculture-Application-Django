from django.db import models

# Create your models here.
class datetime1(models.Model):
    time1=models.TextField(max_length=25)
    class Meta:
        db_table='datatime1'

class contactus(models.Model):
    firstname=models.TextField(max_length=30)
    lastname=models.TextField(max_length=30)
    email=models.EmailField(max_length=30)
    comment=models.TextField(max_length=100)
    class Meta:
        db_table='contactus'

class register(models.Model):
    username=models.TextField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.TextField(max_length=50)
    password=models.TextField(max_length=50)
    is_admin=models.BooleanField(default=False)
    class Meta:
        db_table='register'

class products(models.Model):
    item=models.TextField()
    cost=models.TextField()
    photo=models.ImageField(upload_to='pictures')
    class Meta:
        db_table='products'

class BioData(models.Model):
    firstname=models.TextField()
    lastname=models.TextField()
    dob=models.DateField()
    phone=models.TextField()
    class Meta:
        db_table='BioData'
