from django import forms
from .models import Quiz, Question, Choice

#These classes define the forms that will be used to create a new quiz.
# The exclude variable is used to exclude some fields from the form.
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