# Generated by Django 5.0.3 on 2024-07-18 08:18

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSeeker', '0004_verifyemail_created_at_alter_verifyemail_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('company_url', models.URLField()),
                ('work_done', ckeditor.fields.RichTextField()),
                ('Start_date', models.DateField()),
                ('End_Date', models.DateField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]