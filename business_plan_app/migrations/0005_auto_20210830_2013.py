# Generated by Django 3.2.6 on 2021-08-30 20:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_plan_app', '0004_auto_20210830_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='investment_answer',
        ),
        migrations.AddField(
            model_name='businessplan',
            name='investment_answer',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
