from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

# automated
# new / blank db

from db.models import TimelinePost
User = get_user_model()

class TimelinePostAPITestCase(APITestCase):
	def setUp(self):
		user_obj = User(username='testuser', email='test@test.com')
		user_obj.set_password("password")
		user_obj.save()
		timeline_post = TimelinePost.objects.create(
			user=user_obj,
			track=1,
			description='test'
			)

	def test_single_user(self):
		user_count = User.objects.count()
		self.assertEqual(user_count, 1)