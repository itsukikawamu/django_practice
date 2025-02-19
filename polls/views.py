from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    out_put = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(out_put)

def detail(request, question_id):
    return HttpResponse("you're looking at question %s." %question_id)

def result(request, question_id):
    response  = "you're looking at the results of quesstion %s."
    return HttpResponse(response)

def vote(requests, question_id):
    response = "you're voting on question %s."
    return HttpResponse(response %question_id) 