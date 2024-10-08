# Generated by Django 5.0.3 on 2024-05-18 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0009_alter_withdrawnapplication_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicant',
            name='is_withdrawn',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='withdrawnapplication',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employer.jobapplicant'),
        ),
    ]
