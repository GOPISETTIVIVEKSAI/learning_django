from django.db import models

# Create your models here.
#NAME
class plant(models.Model):
    plant_name = models.TextField(max_length=100)
    scientific_name = models.TextField(max_length=100)
    variety_name = models.TextField(max_length=100)
    prtice = models.IntegerField()
    pic = models.ImageField(null=True)
    imported = models.BooleanField(default=False)