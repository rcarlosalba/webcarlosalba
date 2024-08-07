from django.shortcuts import render
from portafolio import models as portafolio_models
from blog import models as blog_models
# Create your views here.


def index(request):
    all_proyects = portafolio_models.Projects.objects.all()[:3]
    all_posts = blog_models.BlogEntry.objects.all()[:3]
    return render(request, 'pages/index.html', {'proyects': all_proyects,
                                                'posts': all_posts})


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def courses(request):
    context = {}
    return render(request, 'pages/courses.html', context)


def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)


def cv(request):
    context = {}
    return render(request, 'pages/cv.html', context)
