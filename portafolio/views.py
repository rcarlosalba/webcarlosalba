from django.shortcuts import get_object_or_404, render
from .models import Projects


def project_list(request):
    projects = Projects.objects.all()
    return render(request, 'portafolio/projects_list.html', {'projects': projects})


def category(request, category_name):
    category_projects = Projects.objects.filter(
        categories__name__icontains=category_name)
    return render(request, 'portafolio/category.html', {'category_projects': category_projects, 'category_name': category_name})


def project_details(request, slug):
    project = get_object_or_404(Projects, slug=slug)
    return render(request, 'portafolio/project_details.html', {'project': project})
