from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import settings,static
from .yasg import urlpatterns as all_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/',include('core.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
    
]

urlpatterns += all_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
