# Generated by Django 2.2 on 2020-12-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduSystem', '0004_auto_20201211_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Teachers',
            field=models.ManyToManyField(blank=True, related_name='student_teacher', to='eduSystem.Teacher'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='teacher_subject', to='eduSystem.Subject'),
        ),
    ]