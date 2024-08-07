from django.shortcuts import render, get_object_or_404
from random import randint
from .models import BlogEntry
import re


def remove_specific_tags(text, tags):
    for tag in tags:
        # Remove opening and closing tags
        text = re.sub(f'</?{tag}.*?>', '', text)
    return text


def blog(request):
    posts = BlogEntry.objects.all()
    if posts.exists():
        random_entry_index = randint(0, len(posts) - 1)
        highlighted_post = posts[random_entry_index]
        other_posts = posts.exclude(id=highlighted_post.id)

        # Remover etiquetas específicas
        tags_to_remove = ['strong']
        highlighted_post.content = remove_specific_tags(
            highlighted_post.content, tags_to_remove)
        for post in other_posts:
            post.content = remove_specific_tags(post.content, tags_to_remove)

        context = {
            'highlighted_post': highlighted_post,
            'other_posts': other_posts,
        }
    else:
        context = {
            'highlighted_post': None,
            'other_posts': None,
        }
    return render(request, 'blog/blog_list.html', context)


def category(request, category_name):
    category_posts = BlogEntry.objects.filter(
        categories__name__icontains=category_name)
    context = {
        'category_posts': category_posts,
        'category_name': category_name,
    }
    return render(request, 'blog/category.html', context)


def post_details(request, slug):
    post = get_object_or_404(BlogEntry, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_details.html', context)
