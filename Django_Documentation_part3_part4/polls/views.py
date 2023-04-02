from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice


def homepage(request):
    return render(request, 'home.html')


def questions_lists(requests):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(requests, 'polls/questions.html', context=context)
    # questions = Question.objects.all()
    # response = ''
    # for index, question in enumerate(questions):
    #     response += f" {index + 1}. {question.text}<br>"
    # return HttpResponse(f"Questions lists here.<br>{response}")


def question_detail(requests, pk):
    question = get_object_or_404(Question, id=pk)
    choices = Choice.objects.filter(question=question)
    context = {
        'question': question,
        'choices': choices,
    }
    return render(requests, 'polls/question_detail.html', context=context)
    # try:
    #     question = Question.objects.get(id=pk)
    # except Question.DoesNotExist:
    #     raise Http404
    # else:
    #     return HttpResponse(f"Question text: {question.text}<br>pub_date: {question.pub_date}")



# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Question
#
#
# # Create your views here.
#
# def homepage(request):
#     return HttpResponse("<h1>Hello, World. You're at the polls <span style='color:red'>index</span></h1>")
#
#
# def questions_list(request):
#     questions = Question.objects.all()
#     response = ''
#     for index ,question in enumerate(questions):
#         response += f"{index + 1 }. {question.question_text}<br>"
#     return HttpResponse(f"Assalumu Akeykum <br>{response}")
#
# def questions_detail(request, pk):
#     question = Question.objects.get(id= pk)
#     return HttpResponse(f"Question text: {question.question_text}<br>pub_date: {question.pub_date}")