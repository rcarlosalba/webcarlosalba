from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<str:slug>', views.post_details, name='post_details'),
    path('categoria/<str:category_name>',
         views.category, name='category_posts'),
]
