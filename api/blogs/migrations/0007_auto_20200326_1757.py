# Generated by Django 3.0.4 on 2020-03-26 17:57

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200325_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.URLField(default=blogs.models.get_default_url),
        ),
    ]