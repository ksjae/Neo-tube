# Generated by Django 2.2.7 on 2019-12-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
