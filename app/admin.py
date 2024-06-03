from django.contrib import admin
from . import models
# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


admin.site.register(models.Gallery, GalleryAdmin)


admin.site.register(models.HomeScreenImages)


class SubmittedProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'name', 'email')

admin.site.register(models.SubmittedProjects, SubmittedProjectsAdmin)


class SentMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')

admin.site.register(models.SentMessage, SentMessageAdmin)


class ProjectsInProgressAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

admin.site.register(models.ProjectInProgress, ProjectsInProgressAdmin)

admin.site.register(models.About)