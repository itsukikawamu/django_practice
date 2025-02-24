# Generated by Django 5.1.6 on 2025-02-24 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0005_video_external_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
