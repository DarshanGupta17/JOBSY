from django.db import models
from django.utils import timezone
from datetime import timedelta
from ckeditor.fields import RichTextField
# Create your models here.
from account.models import CustomUser
from Employer.models import Skill

class Alert(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " made alert for " + self.skills.name

class VerifyEmail(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    otp = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + 's email verified'
    def is_valid(self):
        now = timezone.now()
        return now <= self.created_at + timedelta(minutes=5)  # Check if the current time is within 5 minutes of the OTP creation time
    
class Jobseeker_Skill(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return self.user.username + " Skills "
    
class Education(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    School = models.CharField(max_length=200)
    Degree = models.CharField(max_length=200)
    Start_date = models.DateField()
    End_date = models.DateField()
    def __str__(self):
        return self.user.username + " education At " + self.School
    

class Experience(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    company_logo = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_url = models.URLField()
    work_done = RichTextField()
    Start_date = models.DateField()
    End_Date = models.DateField(blank=True)
    
    def __str__(self):
        return self.user.username + " experienced in " + self.company_name 
