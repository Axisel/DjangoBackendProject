from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from django.urls import reverse
from django.views.generic import FormView
from .models import Quiz, Question, Choice
from .forms import QuizForm, QuestionForm, ChoiceForm


def index(request):
    template = loader.get_template('index.html')
    context = {
        'quizzes': Quiz.objects.all()
    }
    return HttpResponse(template.render(context, request))


def quiz(request, quizId):
    template = loader.get_template('quiz.html')
    questions = Question.objects.filter(quiz__id=quizId)
    choices = []
    for i in range(len(questions)):
        choices.append(Choice.objects.filter(question__id=questions[i].id))
    context = {
        'quiz': get_object_or_404(Quiz, pk=quizId),
        'quiz_questions': questions,
        'choices': choices,
    }
    return HttpResponse(template.render(context, request))


def quizEditView(request, quizId):
    quiz = get_object_or_404(Quiz, pk=quizId)
    questions = Question.objects.filter(quiz__id=quizId)
    choices = []
    for i in range(len(questions)):
        choices.append(Choice.objects.filter(question__id=questions[i].id))
    context = {
        'quiz': get_object_or_404(Quiz, pk=quizId),
        'quiz_questions': questions,
        'choices': choices,
    }
    return render(request, 'edit.html', context)


def updateQuiz(request, quizId):
    quiz = get_object_or_404(Quiz, pk=quizId)
    questions = Question.objects.filter(quiz_id=quizId)
    qname = request.POST.getlist('question_name')
    cname = request.POST.getlist('choice')

    print("Update request : " + str(request.POST))

    quizname = request.POST['Quizname']
    quizdescription = request.POST.get('Quizdescription')
    quiz.name = quizname
    quiz.description = quizdescription
    choicenb = 0
    questionnb = 0
    for question in questions:

        for choice in Choice.objects.filter(question__id=question.id):
            choice.choice_text = cname[choicenb]
            choice.save()
            choicenb += 1
        question.question_text = qname[questionnb]
        question.save()
        questionnb += 1
    quiz.save()

    return HttpResponseRedirect(reverse('quiz', args=(quizId,)))


def deleteQuiz(request, quizId):
    print("Delete request : " + str(request.POST))
    quiz = get_object_or_404(Quiz, pk=quizId)
    questions = Question.objects.filter(quiz__id=quizId)
    for i in range(len(questions)):
        for c in Choice.objects.filter(question__id=questions[i].id):
            c.delete()
        questions[i].delete()
    quiz.delete()
    return HttpResponseRedirect(reverse('index'))


def new_quiz(request):
     # if this is a POST request we need to process the form data
     if request.method == 'POST':
         if 'name' in request.POST:
             form = QuizForm(request.POST, request.FILES)
         elif 'question_text' in request.POST:
             form = QuestionForm(request.POST)
         else :
             form = ChoiceForm(request.POST)
         # create a form instance and populate it with data from the request:
         # check whether it's valid:
         if form.is_valid():
             # process the data in form.cleaned_data as required
             # ...
             # redirect to a new URL:
             form.save()
             return HttpResponseRedirect('/new-quiz')
         else:
             return render(request, 'form.html', {'form': form, 'form2': QuestionForm, 'form3': ChoiceForm, 'already': True})
     # if a GET (or any other method) we'll create a blank form
     form = QuizForm()
     form2 = QuestionForm()
     form3 = ChoiceForm()

     return render(request, 'form.html', {'form': form, 'form2': form2, 'form3': form3, 'already':False})


class CreateQuizView(FormView):
    template_name = 'form.html'
    form_class = QuizForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateQuestionView(FormView):
    template_name = 'form.html'
    form_class = QuestionForm
    success_url = '/new-quiz'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateChoiceView(FormView):
    template_name = 'form.html'
    form_class = ChoiceForm
    success_url = '/new-quiz'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
