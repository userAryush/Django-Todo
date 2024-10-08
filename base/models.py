from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    description = models.TextField() 
    job_status = models.CharField(max_length=50)
    number = models.IntegerField(null=True, blank=True)
    
