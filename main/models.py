from django.db import models
from ckeditor.fields import RichTextField
# import datetime


class Basics(models.Model):
    class Meta:
        verbose_name_plural = 'Basics'

    web_title = models.CharField(max_length=120, blank=True)
    map = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return f'{self.web_title}'


class Skill(models.Model):
    title = models.CharField(max_length=40, blank=True)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.title} ({self.percent}%)'


class Skill_2(models.Model):
    class Meta:
        verbose_name_plural = 'Skills_2'

    title = models.CharField(max_length=40, blank=True)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.title} ({self.percent}%)'


class Project(models.Model):
    icon = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=50, blank=True)
    text = RichTextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Academy(models.Model):
    class Meta:
        verbose_name_plural = 'Academics'

    icon = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=15, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'

    title = models.CharField(max_length=100, blank=True)
    text = RichTextField(blank=True)
    featured_image = models.ImageField(upload_to='photos/certificates', blank=True)
    date = RichTextField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.title} ({self.text})'


class Information(models.Model):
    class Meta:
        verbose_name_plural = 'Informations'

    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)