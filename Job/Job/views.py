from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from account.forms import LoginForm , SignUpForm
from django.contrib.auth import authenticate,login,logout
from Employer.models import PostJob,JobApplicant

def Home(request):
    return render(request,'main/home.html')

def login_view(request):
    msg = None
    login_form = LoginForm(request.POST or None)
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username = username,password=password)
            if(user is None):
                return redirect('login')
            login(request,user) 
        return redirect('home')
    return render(request,'main/login.html',{'form':login_form})

def logout_view(request):
    logout(request)
    return redirect('login')
    
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created succesfully'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'main/register.html',{'form':form,'msg':msg})

def get_all_jobs(request):
    jobs = PostJob.objects.all()

    return render(request,'main/jobs/alljobs.html',{'jobs':jobs})


def job_detail(request,slug):
    job = PostJob.objects.get(slug=slug)
    try:
        is_applied = JobApplicant.objects.filter(job=job).get(user=request.user).is_applied
        withdrawn = JobApplicant.objects.filter(job=job).get(user=request.user).is_withdrawn
    except JobApplicant.DoesNotExist:
        is_applied = None
        withdrawn = None
    return render(request,'main/jobs/jobdetail.html',{'job':job,'is_applied':is_applied , 'withdrawn':withdrawn})