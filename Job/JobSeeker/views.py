from django.shortcuts import render,redirect,HttpResponse
from Employer.models import PostJob,JobApplicant,WithdrawnApplication,Skill
# Create your views here.
from Employer.decorators import jobseeker_required
from django.contrib.auth.decorators import login_required
from .models import Alert
from django.contrib import messages

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
    except:
        applications = None
    # for i in applications:
    #     print(i.first_name ,i.job.job_title)
    return render(request,'JobSeeker/my_applications.html',{'applications':applications})


def withdraw_applications(request, id):
    application = JobApplicant.objects.get(id = id)
    application.is_applied = False
    application.delete()
    return redirect('JobSeeker:applications')

def create_alert(request):
    skill_id = request.GET.get('skill')
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

