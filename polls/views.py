from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Price


def index(request):
    context = {'title': 'Albion Online Trader Guild'}
    return render(request, 'polls/index.html', context)


def rank(request):
    latest_question_list = Price.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/base.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def renew(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def price(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def profit_all(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def profit_item(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
