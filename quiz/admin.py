#Register your models here.
from django.contrib import admin
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sites.admin import SiteAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import fields
import tablib
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from quiz.models import Type, Quiz, Question_type, Question, Question_option, User,Type, Level

class LevelAdmin(admin.ModelAdmin):
    list_display = ['title']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title']

class ChoiceInline(admin.TabularInline):
    model = Question_option
    extra = 3

class Question_typeAdmin(admin.ModelAdmin):
    list_display = ['title']

class UserAdmin(admin.ModelAdmin):
    list_display = ['email']

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

class QuestionOptionResource(resources.ModelResource):
    full_title = fields.Field()
    class Meta:
        model = Question_option
    def dehydrate_full_title(self, Question_option):
        return '%s' % (Question_option.question.title)

class Question_optionAdmin(ImportExportModelAdmin):
    list_display = ['text']
    resource_class = QuestionOptionResource
    pass
    #resource_class = Question_option

class QuestionAdmin(ImportExportModelAdmin):
    list_display = ['title']
    inlines = [ChoiceInline]
    resource_class = QuestionResource
    list_filter = ('level','quiz',)
    pass

admin.site.register(Level,LevelAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question_type, Question_typeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Question_option, Question_optionAdmin)
admin.site.register(User, UserAdmin)

