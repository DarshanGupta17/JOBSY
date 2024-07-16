from django.shortcuts import render,redirect,HttpResponse
from .models import JobApplicant,PostJob,Skill,Salary
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

# Create your views here.
@jobseeker_required
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
        # print("resume == " , request.FILES['resume'])
        applicant.is_applied = True
        applicant.save()
        messages.success(request , "Application Submitted Successfully")
        return redirect("JobSeeker:applications")

@login_required(login_url="login")
@employer_required
def Applicants(request):
    applications = JobApplicant.objects.filter(author = request.user).order_by('-created_at')
    cntxt = {
        'applicants':applications
    }
    return render(request,"Employer/Applicants.html",cntxt)

@employer_required
def View_Applicant(request,id):
    applicant = JobApplicant.objects.get(id=id)
    print(applicant)
    return render(request,"Employer/viewapplicant.html",{'applicant':applicant})

def searched_result(request):
    search = request.GET.get('search')
    skills = Skill.objects.all()
    skill = Skill.objects.filter(name__icontains = search)
    jobs = PostJob.objects.filter(
        Q(job_title__icontains = search) | Q(company_name__icontains = search) | Q(location__icontains = search)
        | Q(skills__in = skill) | Q(Employment_Type__icontains = search)
    ).distinct()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        selected_skills = request.GET.getlist('skills[]')
        location = request.GET.get('location')
        resulted_jobs=None
        if selected_skills:
            resulted_jobs = jobs.filter(skills__id__in=selected_skills).distinct()
        if location:
            resulted_jobs |= jobs.filter(location__icontains=location)

        jobs_data = []
        if resulted_jobs != None:
            for job in resulted_jobs:
                job_data = {
                    'job_title': job.job_title,
                    'company_name': job.company_name,
                    'location': job.location,
                    'user': job.user.username,
                    'created_at': job.created_at.strftime('%Y-%m-%d') if job.created_at else 'N/A',
                    'slug': job.slug,
                    'skills': [skill.name for skill in job.skills.all()],
                }
                jobs_data.append(job_data)
            print("Json response is being sent")
            return JsonResponse({'jobs': jobs_data})
        else:
            for job in jobs:
                job_data = {
                    'job_title': job.job_title,
                    'company_name': job.company_name,
                    'location': job.location,
                    'user': job.user.username,
                    'created_at': job.created_at.strftime('%Y-%m-%d') if job.created_at else 'N/A',
                    'slug': job.slug,
                    'skills': [skill.name for skill in job.skills.all()],
                }
                jobs_data.append(job_data)
            print("Json response is being sent")
            return JsonResponse({'jobs':jobs_data})    

    # print(jobs)
    return render(request,"main/jobs/alljobs.html",{'jobs':jobs,'search':search,'skill':skills})

@login_required(login_url="login")
@employer_required
def post_job(request):
    digit = str(random.randint(1000,9999))
    if request.method == 'POST':
        job_title = request.POST['job_title']
        job_desc = request.POST['job_desc']
        location = request.POST['location']
        employment_type = request.POST['Employment_Type']
        salary_id = request.POST['salary']
        skills = request.POST.getlist('skills')
        company_name = request.POST['company_name']
        company_info = request.POST['company_info']
        deadline = request.POST['deadline']

        try:
            salary = Salary.objects.get(id=salary_id)

            post_job = PostJob.objects.create(
                user=request.user,
                job_title=job_title,
                job_desc=job_desc,
                location=location,
                Employment_Type=employment_type,
                salary=salary,
                company_name=company_name,
                company_info=company_info,
                deadline=deadline,
                slug=slugify(job_title) + digit
            )
            matching_alert = Alert.objects.filter(skills__in = skills).distinct()
            post_job.skills.set(skills)
            post_job.save()
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
            messages.success(request, 'Job posted successfully!')
            return redirect('allJobs')  # Redirect to the list of jobs or another appropriate view
        except Salary.DoesNotExist:
            messages.error(request, 'Invalid salary selected.')

    skills = Skill.objects.all()
    salaries = Salary.objects.all()

    context = {
        'skills': skills,
        'salaries': salaries
    }
    return render(request, 'Employer/PostJob.html', context)