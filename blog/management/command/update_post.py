from django.core.management.base import BaseCommand
from blog.models import BlogEntry
from django.utils.html import escape


class Command(BaseCommand):
    help = 'Update HTML content of posts'

    def handle(self, *args, **kwargs):
        posts = BlogEntry.objects.all()
        for post in posts:
            post.content = escape(post.content)
            post.save()
        self.stdout.write(self.style.SUCCESS(
            'Successfully updated posts content'))
