# Generic
from rest_framework import generics, mixins

from db.models import TimelinePost
from .permissions import IsOwnerOrReadOnly
from .serializers import TimelinePostSerializer

class TimelinePostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field		= 'post_id'
	serializer_class 	= TimelinePostSerializer

	def get_queryset(self):
		return TimelinePost.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)	

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}

class TimelinePostRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		= 'post_id'
	serializer_class 	= TimelinePostSerializer
	permission_classes  = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return TimelinePost.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}
