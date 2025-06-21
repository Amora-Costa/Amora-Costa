from django.db import models

# Create your models here.
class Registration (models.Model):
    name =models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    Qualification = models.CharField( max_length=50)  
    where_are_you_from = models.CharField(max_length=50) 
    what_type_of_job = models.CharField( max_length=50) 

class Skilled_Jobs(models.Model):
    role = models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    desc = models.TextField()
    
    
class Unskilled_Jobs(models.Model):
    role = models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    desc = models.TextField()
    

class FAQ(models.Model):
    question =models.TextField()

    