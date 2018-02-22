from django.conf.urls import url

from .views import TimelinePostRudView, TimelinePostAPIView

app_name = 'db'
urlpatterns = [
	url(r'^$', TimelinePostAPIView.as_view(), name='post-create'),
	url(r'^(?P<post_id>\d+)/$', TimelinePostRudView.as_view(), name='post-rud')
]