from django.db import models

# Create your models here.
class user(models.Model):
    LastName = models.CharField(max_length=256)
    FirstName = models.CharField(max_length=256)
    email = models.EmailField(max_length=264,unique=True)
    def __str__(self):
        return self.FirstName+' '+self.LastName
