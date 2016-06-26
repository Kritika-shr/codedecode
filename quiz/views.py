
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from quiz.models import Question, Question_option, User, Attempted, Type, Quiz, Level
from django.shortcuts import render, get_object_or_404
from django import forms
from django.shortcuts import get_list_or_404
from django.forms import ModelForm
from django.core.mail import send_mail, BadHeaderError
import json
from django.core import serializers
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

def index(request):
    level_all = Level.objects.all().order_by('order')
    type_all = Type.objects.all()
    return render(request, 'quiz/main-content.html',{'type_all':type_all,'level_all':level_all})


def cat_questions(request, type_id):
    type_all = Type.objects.all()
    quiz = get_object_or_404(Quiz, pk=type_id)
    if quiz.max_time > 60 :
        hour = quiz.max_time / 60
        min = quiz.max_time % 60
    else:
        hour = 0
        min = quiz.max_time
    return render(request, 'quiz/questions.html', {'hour':hour,'min':min, 'quiz':quiz,'type_all':type_all, 'type_id':type_id})

def level_questions(request, level_id):
    level = get_object_or_404(Level, pk=level_id)
    max_time = int(level.max_time)
    if max_time > 60:
        hour = max_time / 60
        min = max_time % 60
    else:
        hour = 0
        min = max_time
    return render(request, 'quiz/question-full.html', {'hour':hour,'min':min, 'level': level})

def login(request):

    if request.method  == 'POST':
        inputEmail = request.POST['inputEmail']
        inputUsername = request.POST['inputUsername']
        inputPassword = request.POST['inputPassword']
    user = User(email=inputEmail,all_info='')
    user.save()
    return render(request, 'quiz/logged-in.html',{'inputEmail':inputEmail})

def exam(request, id):
    level = get_object_or_404(Level, pk=id)
    return render(request, 'quiz/exam.html', {'id':id, 'level':level})


def submit(request):
    option_pk = []
    type_all = Type.objects.all()
    correct_answer_count = 0
    total_question = 0
    if request.method  == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
        if 'type_id' in request.POST:
            id = request.POST['type_id']
            quiz = get_object_or_404(Quiz,pk=id)
            question_attempted = quiz.question_set.all()
            level = 0
            template = 'quiz/submit.html'
        elif 'level_id' in request.POST:
            id = request.POST['level_id']
            level = get_object_or_404(Level,pk=id)
            question_attempted = level.question_set.all()
            template = 'quiz/submit-full.html'
            quiz = ''
        user = User(email=email,all_info='')
        user.save()
        #Get Question as per Quiz Type Attempted
        #Get Correct Answer Count

        for question in question_attempted:
            total_question = total_question + 1
            if('option'+str(question.id)) in request.POST:
                pk = request.POST['option'+str(question.id)]
                option = get_object_or_404(Question_option, pk=pk)
                test_attempted = Attempted(question_id=question.id,option_id=option.id,user_id=int(user.id))
                test_attempted.save()
                if(option.is_correct == 1):
                    if(option.id == test_attempted.option_id):
                        correct_answer_count = correct_answer_count + 1

        user_result = get_list_or_404(Attempted, user_id=user.id)
       # user_result =
        answer= []

        per = (float(correct_answer_count)/total_question)*100
        percentage = round(per,2)
        for result in user_result:
            answer.append(int(result.option_id))
        #return render(request, {'type_id':type_id})
        """try:
            subject, from_email, to = 'mybologsteps: Quiz Result', 'kritika.shrivastava90@gmail.com', email
            text_content = 'This is an important message.'
            html_content = render_to_string('quiz/the_template.html', {'answer':answer ,'correct_answer_count':correct_answer_count,'total_question':total_question})
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        except BadHeaderError:
            return HttpResponse('Invalid header found.')"""

        return render(request, template,{'count':option_pk, 'type_all':type_all, 'question_attempted':question_attempted,'user_id':user.id,'answer':answer ,'correct_answer_count':correct_answer_count,'total_question':total_question,'level':level, 'percentage':percentage, 'quiz':quiz})
    else:
        return index(request)


