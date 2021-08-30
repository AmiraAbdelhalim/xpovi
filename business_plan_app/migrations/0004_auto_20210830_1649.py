# Generated by Django 3.2.6 on 2021-08-30 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_plan_app', '0003_remove_answer_investment_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='investment_answer',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]