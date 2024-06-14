# Generated by Django 5.0.3 on 2024-05-10 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0007_jobapplicant_author_alter_jobapplicant_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawnApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.jobapplicant')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postedEmployer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawnJobseeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]