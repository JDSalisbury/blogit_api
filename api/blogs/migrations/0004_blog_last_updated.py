# Generated by Django 3.0.4 on 2020-03-10 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]