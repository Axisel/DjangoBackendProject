from django import forms
from .models import Quiz, Question, Choice


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = ['pub_date']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = []

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = []