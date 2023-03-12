from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

#The urlpatterns variable is a list of all the urls that the app can handle.
# And the views that will be called when the user access them.
urlpatterns = [
    path('', views.index, name='index'),
    path('new-quiz', views.new_quiz, name='form'),
    path('quiz/<int:quizId>', views.quiz, name='quiz'),
    path('quiz/<int:quizId>/edit-quiz', views.quizEditView, name='edit_quiz'),
    path('quiz/<int:quizId>/update', views.updateQuiz, name='update_quiz'),
    path('quiz/<int:quizId>/delete', views.deleteQuiz, name='delete_quiz'),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
