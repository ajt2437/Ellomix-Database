from rest_framework import serializers

from db.models import TimelinePost

class TimelinePostSerializer(serializers.ModelSerializer):
	url			= serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = TimelinePost
		fields = [
			'url',
			'post_id',
			'user',
			'track',
			'date_posted',
			'description',
		]
		read_only_fields = ['post_id', 'user']

	def get_url(self, obj):
		request = self.context.get("request")
		return obj.get_api_url(request=request)