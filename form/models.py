from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Form(models.Model):
    sponsor = models.CharField(max_length=100)
    sponsored = models.CharField(max_length=100)
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.ImageField(upload_to='form/files')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sponsored + ' was sponsored by ' + self.sponsor + ' for the amount of ' + str(self.amount)