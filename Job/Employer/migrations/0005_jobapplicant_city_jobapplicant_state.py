# Generated by Django 5.0.3 on 2024-05-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0004_jobapplicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicant',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='jobapplicant',
            name='state',
            field=models.CharField(default='', max_length=20),
        ),
    ]