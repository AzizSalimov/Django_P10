from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render


# Create your views here.

def homepage(request):
    return render(request, 'home.html')


def questions_list(request):

 # questions = Question.objects.all()
 # response = ''
 # for index ,question in enumerate(questions):
 #     response += f"{index + 1 }. {question.question_text}<br>"
 # return HttpResponse(f"Assalumu Akeykum <br>{response}")

 questions = Question.objects.all()

 context = {
     'questions': questions
 }
 return render(request, 'polls/questions.html', context=context)



def questions_detail(request, pk):
    # try:
    #     question = Question.objects.get(id=pk)
    # except Question.DoesNotExist:
    #     raise Http404
    # else:
    #     return HttpResponse(f"Question text: {question.question_text}<br>pub_date: {question.pub_date}")
    question = get_object_or_404(Question, id=pk)

    context = {
        'question': question
    }
    return render(request, 'polls/question_detail.html', context= context)