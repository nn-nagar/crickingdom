# Generated by Django 2.2 on 2020-12-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduSystem', '0019_auto_20201211_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
