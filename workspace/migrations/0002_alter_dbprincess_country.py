# Generated by Django 3.2.6 on 2021-08-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbprincess',
            name='country',
            field=models.CharField(max_length=20, verbose_name='unique'),
        ),
    ]
