from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from quiz.models import Quiz, Question, Choice


# The three first tests are used to check if the models are created and read correctly.
class QuizTestCase(TestCase):
    def setUp(self):
        Quiz.objects.create(name="Quiz 1", description="Description 1")
        Quiz.objects.create(name="Quiz 2", description="Description 2")

    def test_Quiz_CreationRead(self):
        quiz1 = Quiz.objects.get(name="Quiz 1")
        quiz2 = Quiz.objects.get(name="Quiz 2")
        self.assertEqual(quiz1.description, "Description 1")
        self.assertEqual(quiz2.description, "Description 2")


class QuestionTestCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        quiz2 = Quiz.objects.create(name="Quiz 2", description="Description 2")
        Question.objects.create(quiz=quiz1, question_text="Question 1")
        Question.objects.create(quiz=quiz2, question_text="Question 2")

    def test_Question_CreationRead(self):
        question1 = Question.objects.get(question_text="Question 1")
        question2 = Question.objects.get(question_text="Question 2")
        self.assertEqual(question1.quiz.name, "Quiz 1")
        self.assertEqual(question2.quiz.name, "Quiz 2")


class ChoiceTestCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        quiz2 = Quiz.objects.create(name="Quiz 2", description="Description 2")
        question1 = Question.objects.create(quiz=quiz1, question_text="Question 1")
        question2 = Question.objects.create(quiz=quiz2, question_text="Question 2")
        Choice.objects.create(question=question1, choice_text="Choice 1")
        Choice.objects.create(question=question2, choice_text="Choice 2")

    def test_Choice_CreationRead(self):
        choice1 = Choice.objects.get(choice_text="Choice 1")
        choice2 = Choice.objects.get(choice_text="Choice 2")
        self.assertEqual(choice1.question.question_text, "Question 1")
        self.assertEqual(choice2.question.question_text, "Question 2")


# The six next tests are used to check if the models are deleted and updated correctly.
class QuizDeleteCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        quiz2 = Quiz.objects.create(name="Quiz 2", description="Description 2")
        quiz1.delete()

    def test_quiz_delete(self):
        quiz1 = Quiz.objects.filter(name="Quiz 1")
        quiz2 = Quiz.objects.get(name="Quiz 2")
        self.assertEqual(quiz1.count(), 0)
        self.assertEqual(quiz2.description, "Description 2")


class QuizUpdateCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        quiz1.name = "Quiz 1 updated"
        quiz1.save()

    def test_quiz_update(self):
        quiz1 = Quiz.objects.get(name="Quiz 1 updated")
        self.assertEqual(quiz1.description, "Description 1")


class QuestionDeleteCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        quiz2 = Quiz.objects.create(name="Quiz 2", description="Description 2")
        question1 = Question.objects.create(quiz=quiz1, question_text="Question 1")
        question2 = Question.objects.create(quiz=quiz2, question_text="Question 2")
        question1.delete()

    def test_question_delete(self):
        question1 = Question.objects.filter(question_text="Question 1")
        question2 = Question.objects.get(question_text="Question 2")
        self.assertEqual(question1.count(), 0)
        self.assertEqual(question2.quiz.name, "Quiz 2")


class QuestionUpdateCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        question1 = Question.objects.create(quiz=quiz1, question_text="Question 1")
        question1.question_text = "Question 1 updated"
        question1.save()

    def test_question_update(self):
        question1 = Question.objects.get(question_text="Question 1 updated")
        self.assertEqual(question1.quiz.name, "Quiz 1")


class ChoiceDeleteCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        question1 = Question.objects.create(quiz=quiz1, question_text="Question 1")
        choice1 = Choice.objects.create(question=question1, choice_text="Choice 1")
        choice2 = Choice.objects.create(question=question1, choice_text="Choice 2")
        choice1.delete()

    def test_choice_delete(self):
        choice1 = Choice.objects.filter(choice_text="Choice 1")
        choice2 = Choice.objects.get(choice_text="Choice 2")
        self.assertEqual(choice1.count(), 0)
        self.assertEqual(choice2.question.question_text, "Question 1")


class ChoiceUpdateCase(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(name="Quiz 1", description="Description 1")
        question1 = Question.objects.create(quiz=quiz1, question_text="Question 1")
        choice1 = Choice.objects.create(question=question1, choice_text="Choice 1")
        choice1.choice_text = "Choice 1 updated"
        choice1.save()

    def test_choice_update(self):
        choice1 = Choice.objects.get(choice_text="Choice 1 updated")
        self.assertEqual(choice1.question.question_text, "Question 1")

# The next tests are used to check if the template and urls are working correctly.
class TemplateTest(TestCase):
    def test_templateIndex(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_templateQuiz(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1",id=2)
        quizBastien.save()
        response = self.client.get(reverse('quiz:quiz', args=(2,)))
        self.assertTemplateUsed(response, 'quiz.html')

    def test_templateForm(self):
        response = self.client.get(reverse('quiz:form'))
        self.assertTemplateUsed(response, 'form.html')

    def test_templateQuizUpdate(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1", id=1)
        quizBastien.save()
        response = self.client.post(reverse('quiz:update_quiz', args=(1,)),  {'Quizname': 'Quiz 1 updated', 'Quizdescription': 'Description 1 updated'})
        self.assertRedirects(response, '/quiz/1')


class ViewTest(TestCase):
    def test_viewIndex(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)

    def test_viewQuiz(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1", id=2)
        quizBastien.save()
        response = self.client.get(reverse('quiz:quiz', args=(2,)))
        self.assertEqual(response.status_code, 200)

    def test_viewQuizFail(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1", id=2)
        response = self.client.get(reverse('quiz:quiz', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_viewForm(self):
        response = self.client.get(reverse('quiz:form'))
        self.assertEqual(response.status_code, 200)

    def test_viewQuizUpdate(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1", id=1)
        quizBastien.save()
        response = self.client.post(reverse('quiz:update_quiz', args=(1,)),  {'Quizname': 'Quiz 1 updated', 'Quizdescription': 'Description 1 updated'})
        self.assertEqual(response.status_code, 302)

    def test_viewQuizUpdateFail(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1", id=1)
        quizBastien.save()
        response = self.client.post(reverse('quiz:update_quiz', args=(2,)),  {'Quizname': 'Quiz 1 updated', 'Quizdescription': 'Description 1 updated'})
        self.assertEqual(response.status_code, 404)



    def test_viewQuizDelete(self):
        quizBastien = Quiz.objects.create(name="Quiz 1", description="Description 1", id=1)
        quizBastien.save()
        response = self.client.post(reverse('quiz:delete_quiz', args=(1,)))
        self.assertEqual(response.status_code, 302)

class LoginTest(TestCase):
    def test_login(self):
        User.objects.create_user('Bastien', 'random@gmail.com', 'BastienP')
        self.client.login(username='Bastien', password='BastienP')
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        User.objects.create_user('Bastien', 'random@gmail.com', 'BastienP')
        self.client.login(username='Bastien', password='BastienP')
        self.client.logout()
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        User.objects.create_user('Bastien', 'random@gmail.com', 'BastienP')
        login = self.client.login(username='Bastien', password='BastienP2')
        self.assertFalse(login)

    def test_signupView(self):
        response = self.client.get(reverse('quiz:accounts:signup'))
        self.assertEqual(response.status_code, 200)

