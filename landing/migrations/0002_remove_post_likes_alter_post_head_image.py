# Generated by Django 4.0.4 on 2022-04-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='landig/images/%Y/%m/%d/%H/'),
        ),
    ]
