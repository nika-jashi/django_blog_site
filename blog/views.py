from django.shortcuts import render
from django.http import HttpResponse

posts =[
    {
        'author': 'nika',
        'title': 'First Blog',
        'content': 'first ever blog',
        'date_posted': 'January 31, 2022'
    },
    {
        'author': 'joe',
        'title': 'Second Blog',
        'content': 'Second ever blog',
        'date_posted': 'february 1, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


