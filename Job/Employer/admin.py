from django.contrib import admin
from .models import PostJob,Salary,Skill,JobApplicant,WithdrawnApplication,StatusOfApplication
# Register your models here.

admin.site.register(PostJob)
admin.site.register(Salary)
admin.site.register(Skill)
admin.site.register(JobApplicant)
admin.site.register(WithdrawnApplication)
admin.site.register(StatusOfApplication)
