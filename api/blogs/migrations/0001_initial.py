# Generated by Django 3.0.4 on 2020-03-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=255)),
                ('picture', models.URLField(default='https://picsum.photos/id/12/300/500')),
                ('body', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('author', models.CharField(default='Jeff Salisbury', max_length=100)),
            ],
        ),
    ]
