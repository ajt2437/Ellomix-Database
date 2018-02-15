# Generic

from rest_framework import generics
from db.models import TimelinePost
from .serializers import TimelinePostSerializer

class TimelinePostRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		= 'post_id'
	serializer_class 	= TimelinePostSerializer

	def get_queryset(self):
		return TimelinePost.objects.all()		