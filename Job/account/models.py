from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_employer = models.BooleanField("Is_Employer",default=False)
    is_jobseeker = models.BooleanField("Is_JobSeeker",default=False)
