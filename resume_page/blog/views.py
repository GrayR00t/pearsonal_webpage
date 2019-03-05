from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'blog/index.html')


def about(request):

    return render(request, 'blog/about.html')


def contact(request):

    return render(request, 'blog/contact.html')

def portfolio(request):

    return render(request, 'blog/portfolio.html')

def portfolio_details(request):

    return render(request, 'blog/portfolio_details.html')

