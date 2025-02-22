from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("you're looking at question %s." %question_id)

def result(request, question_id):
    response  = "you're looking at the results of quesstion %s."
    return HttpResponse(response)

def vote(requests, question_id):
    response = "you're voting on question %s."
    return HttpResponse(response %question_id) 