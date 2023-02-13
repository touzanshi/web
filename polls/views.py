from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_qustion_list = Question.objects.order_by('pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_qustion_list}
    return render(request, template, context)


def detail(request, question_id):
    template = 'polls/detail.html'
    question = get_object_or_404(Question,pk=question_id)

    return render(request, template, context={'question': question})


def results(request, question_id):
    response = 'looking at results of question %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('voting on question %s' % question_id)
