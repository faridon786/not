# Generated by Django 4.2.7 on 2024-04-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_submittedprojects_alter_homescreenimages_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submittedprojects',
            options={'verbose_name_plural': 'Submitted Projects'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='background_image',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='homescreenimages',
            name='images',
            field=models.CharField(max_length=1000),
        ),
    ]
