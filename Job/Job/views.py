from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from account.forms import LoginForm , SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Employer.models import PostJob,JobApplicant,Skill
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers


# @login_required(login_url="login")
def Home(request):
    return render(request,'main/home.html')

def login_view(request):
    msg = None
    login_form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')  # Get the 'next' parameter from the query string
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            next_url = request.POST.get('next')
            if user is None:
                messages.error(request, "Invalid email or password")
                if next_url != "None":
                    return redirect(next_url)
                else:
                    return redirect('login')

            messages.success(request, "Logged in Successfully")
            login(request, user)

            if next_url != "None":  # If there is a next URL, redirect to it
                return redirect(next_url)
            else:
                return redirect('home')

    return render(request, 'main/login.html', {'form': login_form, 'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('login')
    
def register(request):
    msg = None
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # form.is_employer = True
        role = request.POST.get('role')
        if form.is_valid():
            user = form.save(commit=False)  # Create the user instance without saving it to the database yet
            if role == 'J':
                user.is_jobseeker = True
            elif role == 'E':
                user.is_employer = True
            user.save()  # Now save the user to the database
            messages.success(request, "User Created Successfully")
            return redirect('login')
        else:
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{error}")
    else:
        form = SignUpForm()
    return render(request,'main/register.html',{'form':form,'msg':msg})

@login_required(login_url="login")
def get_all_jobs(request):
    jobs = PostJob.objects.all()
    skill = Skill.objects.all()

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

    return render(request, 'main/jobs/alljobs.html', {'jobs': jobs, 'skill': skill})

@login_required(login_url="login")
def job_detail(request,slug):
    job = PostJob.objects.get(slug=slug)
    is_applied = None
    user = request.user
    print(user)
    if user.is_authenticated:
        try:
            is_applied = JobApplicant.objects.filter(job=job).get(user=request.user).is_applied
        except JobApplicant.DoesNotExist:
            is_applied = None
    return render(request,'main/jobs/jobdetail.html',{'job':job,'is_applied':is_applied})

# def fun404(request,exception):
#     return render(request,"404/404.html")

def Profile(request):
    return render(request , "main/profile.html")