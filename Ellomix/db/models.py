from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Users(models.Model):
    user_id             = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=75)
    description         = models.CharField(max_length=500, blank=True, null=True)
    followers_count     = models.IntegerField(blank=True, null=True)
    following_count     = models.IntegerField(blank=True, null=True)
    photo_url           = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.name 

class Track(models.Model):
    track_id            = models.AutoField(primary_key=True)
    artist              = models.CharField(max_length=75, blank=True, null=True)
    title               = models.TextField(blank=True, null=True)
    stream_url          = models.TextField(blank=True, null=True)
    artwork_url         = models.TextField(blank=True, null=True)
    source              = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'

    def __str__(self):
        return self.artist + ' - ' + self.title

class Playlist(models.Model):
    playlist_id         = models.AutoField(primary_key=True)
    track               = models.ForeignKey('Track', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'playlist'

class TimelinePost(models.Model):
    post_id             = models.AutoField(primary_key=True)
    user                = models.ForeignKey('Users', models.DO_NOTHING)
    track               = models.ForeignKey('Track', models.DO_NOTHING)
    date_posted         = models.DateTimeField(blank=True, null=True)
    description         = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timelinepost'

    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse("api-db:post-rud", kwargs={'post_id': self.post_id}, request=request)

class Comment(models.Model):
    user                = models.ForeignKey('Users', models.DO_NOTHING)
    comment             = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'

class Relationship(models.Model):
    follower_id         = models.AutoField(primary_key=True)
    user                = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'relationship'

class Message(models.Model):
    message_id          = models.AutoField(primary_key=True)
    message             = models.TextField(blank=True, null=True)
    user                = models.ForeignKey('Users', models.DO_NOTHING)
    photo_url           = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'

class Chat(models.Model):
    chat_id             = models.AutoField(primary_key=True)
    from_recipent       = models.ForeignKey('Users', models.DO_NOTHING)
    most_recent_message = models.TextField(blank=True, null=True)
    playlist            = models.ForeignKey('Playlist', models.DO_NOTHING)
    message             = models.ForeignKey('Message', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat'


class ChatUsers(models.Model):
    chat_user_id        = models.AutoField(primary_key=True)
    user                = models.ForeignKey('Users', models.DO_NOTHING)
    chat                = models.ForeignKey(Chat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_users'
