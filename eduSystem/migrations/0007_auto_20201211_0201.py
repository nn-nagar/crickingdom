# Generated by Django 2.2 on 2020-12-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduSystem', '0006_auto_20201211_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher_subject', to='eduSystem.Subject'),
        ),
    ]
