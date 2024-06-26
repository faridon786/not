# Generated by Django 4.2.7 on 2024-04-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_submittedprojects_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=5000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
