# Generated by Django 3.2.5 on 2023-01-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaAPI', '0003_auto_20230130_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]