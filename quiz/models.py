from django.db import models
from django.utils.translation import ugettext_lazy as _


enum = lambda *l: [(s,_(s)) for s in l]


class Level(models.Model):
    title = models.CharField(max_length=255)
    max_time = models.CharField(max_length=255)
    order = models.IntegerField(max_length=255)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = "Quiz Level"
        verbose_name_plural = "Quiz Level"

class Type(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField('Created Date')
    is_active = models.BooleanField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Quiz type'
        verbose_name_plural = 'Quizes Type'

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    max_time = models.IntegerField ()
    type = models.ForeignKey('Type')
    position = models.IntegerField()
    created_date = models.DateField('created_date')
    is_active = models.BooleanField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

class Question_type(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateField('created_date')
    is_active = models.BooleanField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Question Type'
        verbose_name_plural = 'Questions Type'

class Question(models.Model):
    level = models.ForeignKey(Level)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quiz = models.ForeignKey(Quiz)
    answer_description = models.CharField(max_length=255)
    question_type = models.ForeignKey(Question_type)
    position = models.IntegerField ()
    created_date = models.DateField('created_date')
    is_active = models.BooleanField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Question_option(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=255)
    position=models.IntegerField()
    is_correct = models.BooleanField()
    def __unicode__(self):
        return self.text
    class Meta:
        verbose_name = 'Question Option'
        verbose_name_plural = 'Questions Option'

class User(models.Model):
    email = models.CharField(max_length=200)
    all_info = models.CharField(max_length=255)
    def __unicode__(self):
        return self.email
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'

class Attempted(models.Model):
    user = models.ForeignKey('user')
    question = models.ForeignKey('Question')
    option = models.ForeignKey('question_option')

class response(models.Model):
    attempt= models.ForeignKey(Attempted)
    user = models.ForeignKey('User')
    quiz = models.ForeignKey('Quiz')
    score  = models.IntegerField()
    quiz_attempt_date = models.DateField()
    time_taken = models.CharField(max_length=255)








# Create your models here.
