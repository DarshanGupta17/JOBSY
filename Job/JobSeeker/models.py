from django.db import models

# Create your models here.
from account.models import CustomUser
from Employer.models import Skill

class Alert(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " made alert for " + self.skills.name
