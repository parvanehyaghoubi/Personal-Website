from django.shortcuts import render
from .models import *

def index(request):
    skills = Skill.objects.all()
    skills_2 = Skill_2.objects.all()
    projects = Project.objects.all()
    academics = Academy.objects.all()
    basics = Basics.objects.all()[0]
    certificates = Certificate.objects.all()

    # print(f'''
    # academics = {academics}
    # ''')
    context ={
        'skills': skills,
        'skills_2': skills_2,
        'projects': projects,
        'academics': academics,
        'basics': basics,
        'certificates': certificates,
    }
    return render(request, template_name='index.html', context=context)