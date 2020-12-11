# Generated by Django 2.2 on 2020-12-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduSystem', '0003_auto_20201211_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Teachers',
            field=models.ManyToManyField(blank=True, null=True, related_name='student_teacher', to='eduSystem.Teacher'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher_subject', to='eduSystem.Subject'),
        ),
    ]
