from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_home/', views.user_home, name='user_home'),
    path('Logout/', views.Logout, name='Logout'),
    path('recruiter_signup/', views.recruiter_signup, name='recruiter_signup'),
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('delete_user/<int:pid>', views.delete_user, name='delete_user'),
    path('delete_recruiter/<int:pid>', views.delete_recruiter, name='delete_recruiter'),
    path('view_users/', views.view_users, name='view_users'),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('change_passwordadmin/', views.change_passwordadmin, name='change_passwordadmin'),
    path('change_passworduser/', views.change_passworduser, name='change_passworduser'),
    path('change_passwordrecruiter/', views.change_passwordrecruiter, name='change_passwordrecruiter'),
    path('add_job/', views.add_job, name='add_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('delete_job/<int:pid>', views.delete_job, name='delete_job'),
    path('edit_jobdetail/<int:pid>', views.edit_jobdetail, name='edit_jobdetail'),
    path('change_companylogo/<int:pid>', views.change_companylogo, name='change_companylogo'),
    path('latest_job/', views.latest_job, name='latest_job'),
    path('user_latestjobs/', views.user_latestjobs, name='user_latestjobs'),
    path('job_detail/', views.job_detail, name='job_detail'),
    path('applyforjob/', views.applyforjob, name='applyforjob'),
    path('contact/', views.contact, name='contact'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('footer/', views.feedback, name='footer'),
    path('applied_candidatelist/', views.applied_candidatelist, name='applied_candidatelist'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)