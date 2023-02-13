from django.shortcuts import render

from django.http import HttpResponse
from .models import Question


def index(request):
    latest_qustion_list = Question.objects.order_by('pub_date')[:5]
    template = 'polls/test.html'
    context = {'latest_question_list': latest_qustion_list}
    return render(request, template, context)


def detail(request, question_id):
    return HttpResponse('looking at question %s' % question_id)


def results(request, question_id):
    response = 'looking at results of question %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('voting on question %s' % question_id)
