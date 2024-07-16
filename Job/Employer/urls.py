from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Employer'

urlpatterns = [
    path('submitApplication/<slug:slug>',views.HandleApplications,name="submitApplication"),
    path('seeApplications',views.Applicants,name="applicants"),
    path('view_applicant/<int:id>',views.View_Applicant,name="viewapplicant"),
    path('searched_result/',views.searched_result , name="searched_result"),
    path('post_a_job/',views.post_job,name="postajob")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)