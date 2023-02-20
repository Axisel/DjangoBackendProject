from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('new-quiz', views.new_quiz, name='form'),
    path('quiz/<int:quizId>', views.quiz, name='quiz'),
    path('quiz/<int:quizId>/edit-quiz', views.quizEditView, name='edit_quiz'),
    path('quiz/<int:quizId>/update', views.updateQuiz, name='update_quiz'),
    path('quiz/<int:quizId>/delete', views.deleteQuiz, name='delete_quiz'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <div class="container-btn">
# <a href="new-quiz" class="btn btn-solid"><span>Create my quiz !</span><i class="fas fa-arrow-right"></i></a>
# </div>