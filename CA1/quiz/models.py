import datetime
from django.db import models
from django.utils import timezone

from django import forms



class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    img = models.ImageField(upload_to='images/', blank=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=100)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=75)
    def __str__(self):
        return self.choice_text
