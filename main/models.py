from django.db import models
import datetime


class Basics(models.Model):
    class Meta:
        verbose_name_plural = 'Basics'

    web_title = models.CharField(max_length=120, blank=True)
    map = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return 'Parvaneh'

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

class Service(models.Model):
    icon = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=50, blank=True)
    text = models.TextField(blank=True)

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

class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=70, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/blog/', blank=True)
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.id} - {self.title} ({self.date})'