# Generated by Django 5.0.3 on 2024-06-23 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0013_postjob_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplicant',
            name='is_withdrawn',
        ),
    ]
