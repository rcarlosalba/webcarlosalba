from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class ProjectCategory(models.Model):
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


class Projects(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = RichTextField(verbose_name='Descripción')
    slug = models.SlugField(verbose_name='Slug', unique=True, blank=True)
    image = models.ImageField(
        upload_to='projects/images/', blank=True, null=True, default='default.jpeg')
    link_repo = models.URLField(
        verbose_name='Enlace Repositorio', blank=True, null=True)
    link_demo = models.URLField(
        verbose_name='Enlace Demo', blank=True, null=True)
    categories = models.ManyToManyField(
        ProjectCategory, verbose_name='Categorías', related_name='get_project')
    created = models.DateTimeField(
        verbose_name='Fecha de Creación', auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name='Fecha de Actualización', auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        # Auto-generar el slug basado en el título
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            queryset = Projects.objects.all()
            counter = 1
            while queryset.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
