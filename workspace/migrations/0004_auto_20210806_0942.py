# Generated by Django 3.2.6 on 2021-08-06 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_auto_20210806_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbcountry',
            name='country',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='dbprincess',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.dbcountry', to_field='country'),
        ),
    ]
