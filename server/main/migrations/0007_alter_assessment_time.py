# Generated by Django 5.0.6 on 2024-07-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_assessment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
