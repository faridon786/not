# Generated by Django 4.2.7 on 2024-04-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='details',
            field=models.TextField(max_length=300),
        ),
    ]
