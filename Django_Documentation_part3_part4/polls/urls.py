from django.urls import path

from polls.views import homepage, questions_list, questions_detail

app_name = 'polls'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_list, name='questions_lists'),
    path('questions/<int:pk>/', questions_detail, name='question_detail')
]

# from django.urls import path
#
# from polls.views import homepage, questions_list, questions_detail
#
# app_name = 'polls'
#
# urlpatterns = [
#     path('information/', homepage, name='homepage'),
#
#     path('questions/', questions_list, name = 'questions_list'),
#
#     path('questions/<int:pk>/', questions_detail, name = 'questionsde_detail')
#
#
# ]

