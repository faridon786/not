# Generated by Django 4.2.7 on 2024-05-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_submittedprojects_project_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('info', models.TextField(max_length=1000)),
                ('image', models.URLField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]