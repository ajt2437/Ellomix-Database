from django.conf.urls import url

from .views import TimelinePostRudView

app_name = 'db'
urlpatterns = [
	url(r'^(?P<post_id>\d+)/$', TimelinePostRudView.as_view(), name='post-rud'),
]