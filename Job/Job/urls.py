"""
URL configuration for Job project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .import views

# handle404 = views.fun404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('',include('account.urls')),
    path('jobseeker/',include('JobSeeker.urls')),
    path('Employer/',include('Employer.urls')),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('register/',views.register,name="register"),
    path('alljobs/',views.get_all_jobs,name="allJobs"),
    path('jobDetail/<slug:slug>',views.job_detail,name="jobdetail"),
    path('profile/',views.Profile,name="profile")

    
]
