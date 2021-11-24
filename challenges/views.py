from typing import List
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response, Http404
from django.urls import reverse
#from django.template.loader import render_to_string

import challenges
# Create your views here.

monthly_challenges = {
    "jan": "janaury bolte",
    "feb": "febraury bolte",
    "mar": None,
    "apr": "april bolte",
    "may": "may bolte",
    "jun": "june bolte",
    "jul": "july bolte",
    "aug": "august bolte",
    "sep": "september bolte",
    "oct": "october bolte",
    "nov": "november bolte",
    "dec": "december bolte"
}

# def jan(request):
#     return HttpResponse('Our jan Page')

# def feb(request):
#     return HttpResponse('this is feb')

def index(request):
    #list_items = ""
    months = list(monthly_challenges.keys())
    
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html", {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('invalid month')
        
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/jan
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        #response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            'text': text,
            'month_name': month
        })
    except:
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
        raise Http404()
    