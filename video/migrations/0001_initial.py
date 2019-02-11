# Generated by Django 2.0.6 on 2019-02-04 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('raw_video_file', models.FileField(upload_to='video/')),
                ('processed', models.BooleanField(default=False)),
                ('mpd_file', models.FilePathField(default=None, null=True)),
            ],
        ),
    ]