from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "JobSeeker"

urlpatterns = [
    path('Apply/<slug:slug>',views.apply,name="apply"),
    path('getapplications',views.get_applications,name="applications"),
    path('withdraw_application/<int:id>',views.withdraw_applications,name="withdraw"),
    path('alertCreate/',views.create_alert ,name="create_alert"),
    path('verifyemail/',views.Verifyemail,name="verifyemail")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)