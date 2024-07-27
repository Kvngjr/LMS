# Generated by Django 5.0.6 on 2024-07-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_grade_answers_alter_grade_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to='materials/'),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('assessment', 'student')},
        ),
    ]
