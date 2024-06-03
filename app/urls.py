from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('submit-project', views.submit_project, name="submit-project"),
    path('projects-in-progress', views.projects_in_progress, name="projects-in-progress")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)