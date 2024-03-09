from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from job_portal.job_portal import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)