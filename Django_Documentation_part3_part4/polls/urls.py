from django.urls import path

from polls.views import homepage, questions_lists, question_detail

app_name = 'polls'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_lists, name='questions_lists'),
    path('questions/<int:pk>/', question_detail, name='question_detail')
]

# from django.urls import path
#
# from polls.views import homepage, questions_list, questions_detail
#
# app_name = 'polls'
#
# urlpatterns = [
#     path('', homepage, name='homepage'),
#
#     path('questions/', questions_list, name = 'questions_list'),
#
#     path('questions/<int:pk>/', questions_detail, name = 'questionsde_detail')
#
#
# ]

