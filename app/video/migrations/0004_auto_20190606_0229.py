# Generated by Django 2.2.2 on 2019-06-06 02:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0003_auto_20190314_0024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyChunkedUpload',
            new_name='VideoChunkedUpload',
        ),
    ]
