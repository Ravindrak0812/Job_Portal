from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Recruiter)
admin.site.register(Job)
admin.site.register(Apply)
admin.site.register(Admin)
admin.site.register(Feedback)