from django.shortcuts import render,redirect,HttpResponse
from Employer.models import PostJob,JobApplicant,WithdrawnApplication,Skill,StatusOfApplication
# Create your views here.
from Employer.decorators import jobseeker_required
from django.contrib.auth.decorators import login_required
from .models import Alert , VerifyEmail
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives , send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Job.settings import EMAIL_HOST_USER

import random

@login_required(login_url="login")
@jobseeker_required
def apply(request,slug):
    job = PostJob.objects.get(slug = slug)
    try:
        details = JobApplicant.objects.get(user = request.user)
    except:
        details = None
    print(details)
    return render(request,'JobSeeker/Applications.html',{'job':job,'details':details})

@login_required(login_url="login")
@jobseeker_required
def get_applications(request):
    try:
        applications = JobApplicant.objects.filter(user = request.user)
        status = StatusOfApplication.objects.filter(user = request.user)
    except:
        applications = None
        status = None
    # for i in applications:
    #     print(i.first_name ,i.job.job_title)
    return render(request,'JobSeeker/my_applications.html',{'status':status})




def withdraw_applications(request, id):
    application = JobApplicant.objects.get(id = id)
    application.is_applied = False
    application.delete()
    return redirect('JobSeeker:applications')

def create_alert(request):
    skill_id = request.POST.get('skill')
    if request.method == "POST":
        print("this is " , skill_id)
        skill = Skill.objects.get(id=skill_id)
        allalerts = Alert.objects.filter(user=request.user, skills=skill)
        if allalerts.exists():
            messages.error(request, f"Alert for {skill.name} already exists")
        else:
            alert = Alert(
                user=request.user,
                skills = skill
            )
            alert.save()
            messages.success(request, f"Alert has been created for {skill.name}")

    return redirect("allJobs")

def generate():
    otp = int(random.randrange(1000,9999))
    return otp

def send (request):
    otp = generate()
    verify = VerifyEmail()
    verify.otp = otp
    verify.user = request.user
    verify.is_verified = False
    verify.save()
    subject = "Verify Your Email At Jobsy"
    r_list = [request.user.email]
    send_mail(subject, f"Your OTP for verifying email address is {otp}", EMAIL_HOST_USER, r_list)

def Verifyemail(request):
    if request.method == "POST":
        try:
            verify = VerifyEmail.objects.get(user=request.user)
        except VerifyEmail.DoesNotExist:
            messages.error(request, "Verification record not found.")
            return redirect('JobSeeker:verifyemail')
        
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        input_otp = int(otp1 + otp2 + otp3 + otp4)
        print(input_otp)
        
        if input_otp == verify.otp and verify.is_valid():
            print('Email verified')
            verify.is_verified = True  # Mark the email as verified
            verify.save()
            messages.success(request, "Your Email has been Verified")
            return redirect("profile")
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return render(request, "main/Profile/verifyemail.html")
    
    # Check if there is a valid OTP already sent
    already_verified = VerifyEmail.objects.filter(user=request.user)
    if already_verified.exists():
        verify = already_verified.first()
        if verify.is_verified:
            return HttpResponse('This User has already been Verified')
        elif verify.is_valid():
            return render(request, "main/Profile/verifyemail.html")
        else:
            verify.delete()  # Delete the expired OTP record
            send(request)  # Send a new OTP

    else:
        send(request)  # Send a new OTP if no valid OTP exists

    return render(request, "main/Profile/verifyemail.html")