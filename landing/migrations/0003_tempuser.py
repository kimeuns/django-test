# Generated by Django 4.0.4 on 2022-04-26 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_remove_post_likes_alter_post_head_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
    ]