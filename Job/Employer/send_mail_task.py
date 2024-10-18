from django.shortcuts import render,redirect,HttpResponse
from .models import JobApplicant,PostJob,Skill,Salary,StatusOfApplication 
from JobSeeker.models import Alert
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.utils.text import slugify
from .forms import PostJobForm
import random
from .decorators import employer_required , jobseeker_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Job.settings import EMAIL_HOST_USER
from account.models import CustomUser
from django.http import JsonResponse
from celery import shared_task

@shared_task
def sendMail(skills,job_title,post_job_id):
    post_job = PostJob.objects.get(id=post_job_id)
    matching_alert = Alert.objects.filter(skills__in = skills).distinct()
    for item in matching_alert:
        subject = f"Your Job Alert for {item.skills}"
        html_content = render_to_string("mails/alert.html",{
            "title":job_title,
            "username":item.user.username,
            "job":post_job
        })
        text_content = strip_tags(html_content)
        r_list = [item.user.email]
        email = EmailMultiAlternatives(subject,text_content,EMAIL_HOST_USER,r_list)
        email.attach_alternative(html_content,"text/html")
        email.send()
    return "success"