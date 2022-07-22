from django.contrib.auth.models import Group
from django.test import TestCase
from django.db.utils import IntegrityError

from authentication.models import User

class TestModels(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='type')
        self.user = User.objects.create(
            email='some@example.com',
        )
        self.user.set_password('complexpassword')
        self.user.groups.add(self.group)
        self.user.save()

    def test_user_type(self):
        user_type = self.user.user_type
        self.assertEqual(user_type, self.group.name)

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(
                email=self.user.email,
            )
