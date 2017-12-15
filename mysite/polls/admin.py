# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice

# https://docs.djangoproject.com/en/1.11/intro/tutorial07/
# 这个没看完，暂时没用，不看了

'''
class QuestionAdmin(admin.ModelAdmin):
     fields = ['pub_date', 'question_text']
'''
'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
'''

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    #model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 这几个改的是问题里显示的东西
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 这行改的是问题列表
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
