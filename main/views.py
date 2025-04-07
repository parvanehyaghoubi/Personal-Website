from django.shortcuts import render
from .models import *

def index(request):
    skills = Skill.objects.all()
    skills_2 = Skill_2.objects.all()
    services = Service.objects.all()
    academics = Academy.objects.all()
    basics = Basics.objects.all()
    posts = Blog.objects.order_by('-date')[:4]
    # print(f'''
    #         {type(posts)}
    #     ''')


    context ={
        'skills': skills,
        'skills_2': skills_2,
        'services': services,
        'academics': academics,
        'basics': basics,
        'posts': posts,
    }
    return render(request, template_name='index.html', context=context)