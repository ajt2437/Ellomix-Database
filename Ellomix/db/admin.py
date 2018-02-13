from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(TimelinePost)
admin.site.register(Comment)
admin.site.register(Relationship)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(ChatUsers)