# Generated by Django 3.2.5 on 2023-01-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaAPI', '0005_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='userid',
            field=models.IntegerField(default=1),
        ),
    ]
