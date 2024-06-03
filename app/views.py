from django.shortcuts import render, get_object_or_404
from . import models
from django.urls import reverse
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
import smtplib


# Create your views here.


def index(request):
    images = models.HomeScreenImages.objects.all()
    return render(request, 'index.html', {'images': images})


def about(request):
    about = models.About.objects.all()
    return render(request, 'about.html', {'abouts': about})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        message = models.SentMessage.objects.create(name=name, email=email, message=message)
        message.save()

        return HttpResponse('<h2>Your message was sent successfully. <br> Thanks for contacting us</h2>')
    else:
        return render(request, 'contact.html')


def gallery(request):
    profiles = models.Gallery.objects.all()
    return render(request, 'gallery.html', {"profiles": profiles})


def submit_project(request):
    images = models.HomeScreenImages.objects.all()
    submitted_projects = models.SubmittedProjects.objects.all()
    if request.method == 'POST':
        project_name = request.POST['projectName']
        email = request.POST['email']
        name = request.POST['name']
        project_info = request.POST['projectInfo']

        models.SubmittedProjects.objects.create(project_name=project_name,
                                                email=email,
                                                name=name,
                                                project_info=project_info
        ).save

        return HttpResponse('<h1>Your Project has been submitted successfully. <br> You will get a respone back within 3-4 hours</h1>')

    else:
        return render(request, 'submit-project.html', {'images': images})

def projects_in_progress(request):
    projects = models.ProjectInProgress.objects.all()

    return render(request, 'projects-in-progress.html', {'projects': projects})