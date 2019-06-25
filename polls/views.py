from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'title': 'Albion Trader - Make your big money'}
    return render(request, 'polls/index.html', context)


def contact(request):
    context = {
        'title': 'Albion Trader Guild - Contact',
        'hero_title': 'Contact',
        'hero_subtitle':'Don\'t kill me (ToT)'
    }
    return render(request, 'polls/contact.html', context)


def rank(request):
    context = {'title': 'Albion Trader - Analyze'}
    return render(request, 'polls/rank.html', context)


def about(request):
    context = {'title': 'Albion Trader - About me'}
    return render(request, 'polls/about.html', context)


def license_(request):
    context = {
        'title': 'Albion Trader - License',
        'hero_title': 'License',
        'hero_subtitle': 'I agree and respect the following.'
    }
    return render(request, 'polls/license.html', context)


def renew(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def price(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def profit_all(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def profit_item(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
