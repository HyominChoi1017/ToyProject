# Generated by Django 3.2.5 on 2023-01-15 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='User', max_length=20)),
                ('Name', models.CharField(default='noname', max_length=20)),
                ('Password', models.CharField(default='', max_length=20)),
                ('ProfileImg', models.ImageField(upload_to='ProfileImg')),
                ('favData', models.JSONField(default={'album': [], 'artist': [], 'music': []})),
                ('relationShip', models.JSONField(default={'follower': [], 'following': []})),
                ('intrestedPost', models.JSONField(default={'likedPost': [], 'savedPost': []})),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AlbumCover', models.URLField()),
                ('MusicData', models.URLField()),
                ('Content', models.CharField(default='', max_length=300)),
                ('User_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='instaAPI.user')),
            ],
        ),
    ]