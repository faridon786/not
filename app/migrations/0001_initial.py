# Generated by Django 4.2.7 on 2024-04-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('background_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
