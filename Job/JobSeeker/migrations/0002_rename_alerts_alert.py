# Generated by Django 5.0.3 on 2024-07-12 08:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0021_alter_postjob_slug'),
        ('JobSeeker', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='alerts',
            new_name='Alert',
        ),
    ]
