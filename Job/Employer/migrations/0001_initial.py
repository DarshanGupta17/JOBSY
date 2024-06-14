# Generated by Django 5.0.3 on 2024-05-05 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=200)),
                ('job_desc', models.TextField()),
                ('location', models.CharField(default='', max_length=300)),
                ('Employment_Type', models.CharField(choices=[('I', 'InterShip'), ('P', 'PartTime'), ('F', 'FullTime')], max_length=20)),
                ('company_info', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('expired', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.salary')),
                ('skills', models.ManyToManyField(related_name='skills', to='Employer.skill')),
            ],
        ),
    ]