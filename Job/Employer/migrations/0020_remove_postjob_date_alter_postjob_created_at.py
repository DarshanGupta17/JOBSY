# Generated by Django 5.0.3 on 2024-07-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0019_jobapplicant_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='date',
        ),
        migrations.AlterField(
            model_name='postjob',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
