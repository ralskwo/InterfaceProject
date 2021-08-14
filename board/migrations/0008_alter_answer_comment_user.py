# Generated by Django 3.2.6 on 2021-08-14 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0007_answer_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]