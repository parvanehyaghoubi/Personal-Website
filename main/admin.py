from django.contrib import admin
from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'percent']
    list_display_links = ['id', 'title']
    list_editable = ['percent']


class Skill_2_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'percent']
    list_display_links = ['id', 'title']
    list_editable = ['percent']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon']
    list_display_links = ['id', 'title']
    list_editable = ['icon']


class AcademyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon']
    list_display_links = ['id', 'title']
    list_editable = ['icon']


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


class InformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'email', 'linkedin', 'github']
    list_display_links = ['id', 'phone', 'email', 'linkedin', 'github']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Skill_2, Skill_2_Admin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Academy, AcademyAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(Basics)
