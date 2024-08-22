from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Alert)
admin.site.register(VerifyEmail)
admin.site.register(Experience)
admin.site.register(Jobseeker_Skill)
admin.site.register(Education)