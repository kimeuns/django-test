# Generated by Django 4.0.4 on 2022-04-25 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boot', '0002_remove_inquiry_created_at_remove_inquiry_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
