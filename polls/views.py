from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Price


def index(request):
    context = {'title': 'Albion Trader - Make your big money'}
    return render(request, 'polls/index.html', context)


def contact(request):
    context = {
        'title': 'Albion Trader Guild - Contact',
        'home_title': 'Albion Trader Guild'
    }
    return render(request, 'polls/contact.html', context)


def rank(request):
    context = {'title': 'Albion Trader - Analyze'}
    return render(request, 'polls/index.html', context)


def renew(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def price(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def profit_all(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def profit_item(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
