from django.db import models

# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    background_image = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Galleries"

# Photo Sizes must be 1280x961
class HomeScreenImages(models.Model):
    images = models.CharField(max_length=1000)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Home Screen Images'


class SubmittedProjects(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    project_name = models.CharField(max_length=50)
    project_info = models.TextField(max_length=10000)

    class Meta:
        verbose_name_plural = 'Submitted Projects'


class SentMessage(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now=True)


class ProjectInProgress(models.Model):
    title = models.CharField(max_length=30)
    info = models.TextField(max_length=1000)
    image = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Projects in Progress'


class About(models.Model):
    about = models.TextField(max_length=1000)
    
    class Meta:
        verbose_name_plural = 'About'