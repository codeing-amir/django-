from django.contrib import admin
from .models import *

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    search_fields = ['name', 'title', 'email']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'university', 'field', 'start_date', 'end_date']
    list_filter = ['university', 'start_date']
    search_fields = ['degree', 'university']

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['company', 'start_date', 'is_current']
    search_fields = ['title', 'company']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    search_fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'start_date', 'is_active']
    list_filter = ['technologies', 'start_date', 'is_active']
    search_fields = ['title', 'technologies']

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url']
    list_filter = ['platform']
