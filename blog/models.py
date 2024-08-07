from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User


class CategoryEntry(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nombre de la Categoría')
    slug = models.SlugField(verbose_name='Slug', unique=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    meta_title = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Meta Título')
    meta_description = RichTextField(
        blank=True, null=True, verbose_name='Meta Descripción')
    keywords = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Palabras Clave')
    featured_image_autor = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Nombre del Autor de la Imagen Destacada')
    featured_image_url = models.URLField(
        blank=True, null=True, verbose_name='URL de la Imagen Destacada')
    featured_image = models.ImageField(
        upload_to='blog/images/', blank=True, null=True, default='default.jpeg')
    categories = models.ManyToManyField(
        CategoryEntry, verbose_name='Categorías', related_name='get_post')
    published = models.DateTimeField(
        verbose_name='Fecha de publicación', default=now)
    created = models.DateTimeField(
        verbose_name='Fecha de Creación', auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name='Fecha de Actualización', auto_now=True)

    def save(self, *args, **kwargs):
        # Auto-generar el slug basado en el título
        if not self.slug:
            self.slug = slugify(self.title)
            # Manejo de unicidad del slug
            original_slug = self.slug
            queryset = BlogEntry.objects.all()
            counter = 1
            while queryset.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Entrada de Blog'
        verbose_name_plural = 'Entradas de Blog'
        ordering = ['-published']

    def __str__(self):
        return self.title
