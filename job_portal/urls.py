from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job.urls'))
]
