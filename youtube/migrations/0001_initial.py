# Generated by Django 5.1.6 on 2025-02-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(blank=True, max_length=225, null=True, unique=True)),
                ('subscribers_number', models.PositiveBigIntegerField(default=0, verbose_name='登録者数')),
            ],
        ),
    ]
