from django.contrib import admin
from .models import MyUser, PlaylistModle
from .models import (
    User, Post, Comment
    )

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'Username',
        'Password',
    )

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(MyUser)
admin.site.register(PlaylistModle)


