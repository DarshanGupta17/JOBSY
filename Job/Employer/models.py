from django.db import models
from account.models import CustomUser
from django.utils.text import slugify

# Create your models here.

class Salary(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.start,self.end)
    
class Skill(models.Model):
    name = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name

class PostJob(models.Model):
    employment_choice = [
        ('Internship','InterShip'),
        ('PartTime','PartTime'),
        ('Fulltime','FullTime')
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200,default="")
    job_desc = models.TextField()
    location = models.CharField(max_length=300,default="")
    Employment_Type = models.CharField(choices=employment_choice,max_length=20)
    salary = models.ForeignKey(Salary,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill,related_name="skills")
    company_name = models.CharField(max_length=50,default="")
    company_info = models.TextField()
    deadline = models.DateTimeField()
    expired = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} ---> {}'.format(self.job_title,self.user.username)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.job_title)
        super(PostJob, self).save(*args, **kwargs)
    
class JobApplicant(models.Model):
    gender_choice = [
        ("M","Male"),
        ("F",'Female'),
        ("O","Other")
    ]
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE,related_name="jobseeker")
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="employer")
    job = models.ForeignKey(PostJob,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=200,default="")
    city = models.CharField(max_length=20,default="")
    state = models.CharField(max_length=20,default="")
    zip = models.IntegerField()
    gender = models.CharField(choices=gender_choice,max_length=20)
    skills = models.CharField(max_length=200,default="")
    resume = models.FileField(upload_to="Resume")
    is_applied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.user.username,self.job.job_title)

class StatusOfApplication(models.Model):
    choice = [
        ('s','shortlist'),
        ('u','underProcess'),
        ('r','rejected'),
        ('p','pending')
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status = models.CharField(choices=choice,max_length=20)
    applicant = models.ForeignKey(JobApplicant,on_delete=models.CASCADE)

    def __str__(self):
        return '{}-for-{}'.format(self.status,self.applicant.first_name)

class WithdrawnApplication(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="withdrawnJobseeker")
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="postedEmployer")
    application = models.ForeignKey(JobApplicant,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - posted by - {} - withdrawn by {}'.format(self.application.job.job_title,self.author.username,self.user.username)


