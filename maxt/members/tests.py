import os
from django.test import TestCase
from django.contrib.auth.models import User

from . templatetags.member_filters import active_page_class
from . models import Member


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                 email='testuser@example.com',
                                 password='foobar')
        self.member = Member.objects.create(user=self.user)

    def test_member(self):
        self.assertTrue(isinstance(self.member, Member))
        self.assertEqual(self.member.__str__(), self.user.username)


class FilterTests(TestCase):

    def test_active_page_class(self):
        active_page = 'class="active"'
        inactive_page = ''
        testIO = (
            {
                'page': "/",
                'request_url': "/",
                'expected': active_page,
            },
            {
                'page': "/tools/",
                'request_url': "/tools/",
                'expected': active_page,
            },
            {
                'page': "/user/",
                'request_url': "/user/foobar/",
                'expected': active_page,
            },
            {
                'page': "/",
                'request_url': "/tools/",
                'expected': inactive_page,
            },
            {
                'page': "/tools/",
                'request_url': "/users/",
                'expected': inactive_page,
            },
        )

        for t in testIO:
            val = active_page_class(t['request_url'], t['page'])
            self.assertIn(t['expected'], val)
