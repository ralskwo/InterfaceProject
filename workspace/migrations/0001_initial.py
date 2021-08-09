# Generated by Django 3.2.6 on 2021-08-06 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBCountry',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=20, unique=True)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='DBPrincess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField(null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.dbcountry', to_field='country')),
            ],
        ),
        migrations.CreateModel(
            name='DBSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.TextField(null=True)),
                ('song_link', models.TextField(null=True)),
                ('princess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.dbprincess')),
            ],
        ),
        migrations.CreateModel(
            name='DBScene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.TextField(null=True)),
                ('scene_link', models.TextField(null=True)),
                ('princess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.dbprincess')),
            ],
        ),
        migrations.CreateModel(
            name='DBQuoats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoats', models.TextField()),
                ('princess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.dbprincess')),
            ],
        ),
        migrations.CreateModel(
            name='DBInfomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('personality', models.TextField()),
                ('characteristic', models.TextField()),
                ('princess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.dbprincess')),
            ],
        ),
    ]