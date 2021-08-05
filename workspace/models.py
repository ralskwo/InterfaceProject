from django.db import models

# Create your models here.

class DBPrincess(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=20)

class DBCountry(models.Model):
    country = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)

class DBQuoats(models.Model):
    princess_id = models.CharField(max_length=15)
    quoats = models.TextField()

class DBScene(models.Model):
    name = models.CharField(max_length=15)
    scenes = models.TextField()

class DBSong(models.Model):
    name = models.CharField(max_length=15)
    songs = models.TextField()

class DBInfomation(models.Model):
    name = models.CharField(max_length=15)
    info = models.TextField()
    personality = models.TextField()
    characteristic = models.TextField()