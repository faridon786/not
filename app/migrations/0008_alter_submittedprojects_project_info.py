# Generated by Django 4.2.7 on 2024-04-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_sentmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedprojects',
            name='project_info',
            field=models.TextField(max_length=10000),
        ),
    ]
