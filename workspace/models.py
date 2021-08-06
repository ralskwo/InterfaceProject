from django.db import models

# Create your models here.

class DBCountry(models.Model):
    country = models.CharField(max_length=20, unique=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)

class DBPrincess(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    country = models.ForeignKey(DBCountry, to_field='country', on_delete=models.CASCADE)

class DBQuoats(models.Model):
    princess = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    quoats = models.TextField()

class DBScene(models.Model):
    scene = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    scenes = models.TextField()

class DBSong(models.Model):
    song = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    songs = models.TextField()

class DBInfomation(models.Model):
    infoname = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    info = models.TextField()
    personality = models.TextField()
    characteristic = models.TextField()