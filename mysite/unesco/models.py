from django.db import models

# Create your models here.

class Iso(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class States(models.Model):
    name = models.CharField(max_length = 200)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sites(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    justification = models.CharField(max_length=1000)
    year = models.IntegerField(null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    state = models.ForeignKey('States', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
