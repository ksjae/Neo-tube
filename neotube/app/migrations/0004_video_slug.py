# Generated by Django 2.2.7 on 2019-11-26 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191119_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
