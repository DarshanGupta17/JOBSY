from django.shortcuts import render,redirect,HttpResponse
from Employer.models import PostJob,JobApplicant,WithdrawnApplication
# Create your views here.

def apply(request,slug):
    job = PostJob.objects.get(slug = slug)
    try:
        details = JobApplicant.objects.get(user = request.user)
    except:
        details = None
    print(details)
    return render(request,'JobSeeker/Applications.html',{'job':job,'details':details})

def get_applications(request):
    try:
        applications = JobApplicant.objects.filter(user = request.user)
    except:
        applications = None
    for i in applications:
        print(i.first_name ,i.job.job_title , i.is_withdrawn)
    return render(request,'JobSeeker/my_applications.html',{'applications':applications})


def withdraw_applications(request, id):
    application = JobApplicant.objects.get(id = id)
    application.is_withdrawn = True
    application.is_applied = False
    application.delete()
    application.save()
    print(application , " this is withdrawn")
    return redirect('JobSeeker:applications')

