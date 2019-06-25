from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    context = {
        'title': 'Albion Trader - Make your big money'
    }
    return render(request, 'polls/index.html', context)


def contact(request):
    context = {
        'title': _('Albion Trader - Contact'),
        'hero_title': _('Contact'),
        'hero_subtitle': _('Don\'t kill me (ToT)')
    }
    return render(request, 'polls/contact.html', context)


def rank(request):
    context = {
        'title': _('Albion Trader - Analyze')
    }
    return render(request, 'polls/rank.html', context)


def about(request):
    context = {
        'title': _('Albion Trader - About'),
        'hero_title': _('About'),
        'hero_subtitle': _('Head to happiness')
    }
    return render(request, 'polls/about.html', context)


def license_(request):
    context = {
        'title': _('Albion Trader - License'),
        'hero_title': _('License'),
        'hero_subtitle': _('I agree and respect the following')
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
