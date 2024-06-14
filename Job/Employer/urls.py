from django.urls import path , include
from .import views

app_name = 'Employer'

urlpatterns = [
    path('submitApplication/<slug:slug>',views.HandleApplications,name="submitApplication"),
    path('seeApplications',views.Applicants,name="applicants"),
    path('view_applicant/<int:id>',views.View_Applicant,name="viewapplicant")
]