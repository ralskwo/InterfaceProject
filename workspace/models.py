from django.db import models

# Create your models here.

class DBCountry(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=20, unique=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    def __str__(self):
        return f"id={self.id}, country={self.country}, latitude={self.latitude}, longitude={self.longitude}"

class DBPrincess(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    country = models.ForeignKey(DBCountry, on_delete=models.CASCADE)
    def __str__(self):
        return f"id={self.id}, name={self.name}, age={self.age}, country={self.country}"


class DBQuoats(models.Model):
    princess = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    quoat_eng = models.TextField(null=True)
    quoat_kor = models.TextField(null=True)
    def __str__(self):
        return f"princess={self.princess}, quoat_eng={self.quoat_eng}, quoat_kor={self.quoat_kor}"


class DBScene(models.Model):
    princess = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    scene_name = models.TextField(null=True)
    scene_link = models.TextField(null=True)
    def __str__(self):
        return f"princess={self.princess}, scene_name={self.scene_name}, scene_link={self.scene_link}"


class DBSong(models.Model):
    princess = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    song_name = models.TextField(null=True)
    song_link = models.TextField(null=True)
    def __str__(self):
        return f"princess={self.princess}, song_name={self.song_name}, song_link={self.song_link}"


class DBInfomation(models.Model):
    princess = models.ForeignKey(DBPrincess, on_delete=models.CASCADE)
    info = models.TextField()
    personality = models.TextField()
    characteristic = models.TextField()
    def __str__(self):
        return f"princess={self.princess}, info={self.info}, personality={self.personality}, characteristic={self.characteristic}"
