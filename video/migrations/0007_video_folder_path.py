# Generated by Django 2.0.6 on 2019-03-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20190307_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='folder_path',
            field=models.TextField(null=True),
        ),
    ]
