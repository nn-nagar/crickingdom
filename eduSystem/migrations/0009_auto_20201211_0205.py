# Generated by Django 2.2 on 2020-12-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduSystem', '0008_auto_20201211_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(related_name='teacher_subject', to='eduSystem.Subject'),
        ),
    ]
