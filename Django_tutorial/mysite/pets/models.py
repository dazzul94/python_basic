from django.db import models

# Create your models here.
class Pet(models.Model):
  pet_name = models.CharField(max_length=100)