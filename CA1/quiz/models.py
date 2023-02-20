import datetime
from django.db import models
from django.utils import timezone

from django import forms


# This class define the main model of the app, thz Quiz. It has a name, a description, a date of publication and an image.
# The pub_date is automatically set to the current date when the quiz is created.
# The was_published_recently method is used to check if the quiz was published less than a day ago.
# The __str__ method is used to display the name of the quiz in the admin page.
class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    img = models.ImageField(upload_to='images/', blank=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.name

# This class define the model of the questions. It is related to a quiz and has a text.
# As for the quiz, the __str__ method is used to display the text of the question in the admin page.
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=100)

    def __str__(self):
        return self.question_text

# This class define the model of the choices. It is related to a question and has a text.
#As for the quiz and the question, the __str__ method is used to display the text of the choice in the admin page.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=75)
    def __str__(self):
        return self.choice_text
