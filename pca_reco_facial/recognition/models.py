from django.db import models

# Create your models here.

class Face(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="faces/")
    
    def __str__(self):
        return self.name
