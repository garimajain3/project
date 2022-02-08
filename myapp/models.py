
from django.db import models

class Jain(models.Model):
    Name = models.CharField(max_length=50,unique=True)
    
    Email = models.EmailField()
    Subject= models.CharField(max_length=100)
    Message= models.CharField(max_length=500)
    
    def __str__(self):
        return self.Name

