# Generated by Django 3.2 on 2021-04-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YoutubeAPICall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='ChannelTitle',
            field=models.CharField(default='channelName', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='videoID',
            field=models.CharField(default='xt29sY88sdG', max_length=255),
            preserve_default=False,
        ),
    ]
