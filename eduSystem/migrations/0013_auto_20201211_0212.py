# Generated by Django 2.2 on 2020-12-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduSystem', '0012_auto_20201211_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
