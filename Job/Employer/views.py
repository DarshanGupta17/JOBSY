from django.shortcuts import render,redirect,HttpResponse
from .models import JobApplicant,PostJob

# Create your views here.

def HandleApplications(request,slug):
    if request.method == "POST":
        applicant = JobApplicant()
        job = PostJob.objects.get(slug = slug)
        applicant.user = request.user
        applicant.job = job
        applicant.author = job.user
        applicant.first_name = request.POST.get('first_name')
        applicant.last_name = request.POST.get('last_name')
        applicant.city = request.POST.get('city')
        applicant.state = request.POST.get('state')
        applicant.gender = request.POST.get('gender')
        applicant.zip = request.POST.get('zip')
        applicant.skills = request.POST.get('skills')
        applicant.address = request.POST.get('address')
        applicant.resume = request.FILES.get('resume')
        applicant.is_applied = True
        applicant.save()
        return redirect("JobSeeker:applications")

def Applicants(request):
    applications = JobApplicant.objects.filter(author = request.user)
    cntxt = {
        'applicants':applications
    }
    return render(request,"Employer/Applicants.html",cntxt)

def View_Applicant(request,id):
    applicant = JobApplicant.objects.get(id=id)
    print(applicant)
    return render(request,"Employer/viewapplicant.html",{'applicant':applicant})

