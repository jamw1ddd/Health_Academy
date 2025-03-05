# Generated by Django 5.1.4 on 2025-03-02 12:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='next_appointment_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
