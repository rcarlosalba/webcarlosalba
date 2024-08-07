from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='portafolio'),
    path('project/<str:slug>', views.project_details, name='project_details'),
    path('categoria/<str:category_name>',
         views.category, name='category_project'),
]
