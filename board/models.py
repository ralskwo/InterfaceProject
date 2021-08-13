from django.db import models
from django.conf import settings


class Question(models.Model) :
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


# Create your models here.
