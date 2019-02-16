import os
from django.test import TestCase
from . templatetags.member_filters import active_page_class


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
        )

        for t in testIO:
            val = active_page_class(t['request_url'], t['page'])
            self.assertIn(t['expected'], val)
