# DjangoBackendProject - Quiz website

Kipo Quiz is a website that I coded using Django, this framework allowed me to implement CRUD fonctionnalities on this quiz application.

The purpose of this website is to display quiz created by users. Users can create new quiz, edit the questions and choice of these quiz and delete them. The users can add an illustration photo, a description and a title to the quiz, alongside with of course questions and their possible choices.

For the moment user can't do the quiz but this function will be implemented. There also will be a leaderboard to see the best users on each quiz.

This Django test suite contains a series of tests to ensure the correct functioning of the Quiz, Question and Choice models in the quiz application. The tests are organized into two groups: creation and reading tests and deletion and update tests.

The first group of tests consists of the QuizTestCase, QuestionTestCase, and ChoiceTestCase. These tests check if the models are created and read correctly. They create instances of the models and test if the attributes have the expected values.

The second group of tests consists of the QuizDeleteCase, QuizUpdateCase, QuestionDeleteCase, QuestionUpdateCase, ChoiceDeleteCase, and ChoiceUpdateCase. These tests check if the models are deleted and updated correctly. They create instances of the models, modify them, and test if the modifications are reflected in the database.

Each test case is a subclass of Django's TestCase class. The setUp method is called before each test, and it sets up the database with the required data. Each test method checks if the behavior of the model is as expected. They do so by using assertions, which raise an exception if the condition is not met, indicating that the test has failed.

The tests use the Django ORM to create, read, update and delete instances of the models. They also use the Python os module to set the DJANGO_SETTINGS_MODULE environment variable to the quiz.settings_tests module. This module contains the settings used during the tests, which are different from the settings used in production. Finally, the multiprocessing.connection module is imported to allow the tests to communicate with other processes.

Overall, these tests ensure that the Quiz, Question and Choice models in the quiz application are correctly implemented and working as expected.
