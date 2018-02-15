from rest_framework import serializers
from db.models import TimelinePost

class TimelinePostSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimelinePost
		fields = [
			'post_id',
			'user',
			'track',
			'date_posted',
			'description',
		]