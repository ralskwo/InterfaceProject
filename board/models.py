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
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.id}, {self.question}, {self.content}, {self.create_date}, {self.comment_user}"

# Create your models here.
