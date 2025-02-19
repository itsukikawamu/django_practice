from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,  you're at the polls index.")

def detail(request, question_id):
    return HttpResponse("you're looking at question %s." %question_id)

def result(request, question_id):
    response  = "you're looking at the results of quesstion %s."
    return HttpResponse(response)

def vote(requests, question_id):
    response = "you're voting on question %s."
    return HttpResponse(response %question_id) 