from django.contrib import admin
from django.urls import path , include
from .import views

app_name = "JobSeeker"

urlpatterns = [
    path('Apply/<slug:slug>',views.apply,name="apply"),
    path('getapplications',views.get_applications,name="applications"),
    path('withdraw_application/<int:id>',views.withdraw_applications,name="withdraw")
]