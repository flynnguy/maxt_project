from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from members.models import Member
from . models import Section, Brand, Tool


class ModelTests(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name="Woodworking")
        self.brand = Brand.objects.create(name="Delta")
        self.tool = Tool.objects.create(brand=self.brand, name="Saw", section=self.section)

        self.no_brand_tool = Tool.objects.create(name="No Name", section=self.section)

    def test_member(self):
        self.assertTrue(isinstance(self.section, Section))
        self.assertEqual(self.section.__str__(), "Woodworking")

    def test_branc(self):
        self.assertTrue(isinstance(self.brand, Brand))
        self.assertEqual(self.brand.__str__(), "Delta")

    def test_tool(self):
        self.assertTrue(isinstance(self.tool, Tool))
        self.assertEqual(self.tool.__str__(), "Delta Saw")

        self.assertTrue(isinstance(self.no_brand_tool, Tool))
        self.assertEqual(self.no_brand_tool.__str__(), "No Name")


class ViewsTests(TestCase):

    def setUp(self):
        self.section = Section.objects.create(name="Woodworking")
        self.brand = Brand.objects.create(name="Delta")
        self.tool = Tool.objects.create(brand=self.brand, name="Saw", section=self.section)
        
        self.user = User.objects.create_user(username='testadmin',
                                 email='testuser@example.com',
                                 is_superuser=True,
                                 password='foobar')

        self.member = Member.objects.create(user=self.user)

    def test_tools_index(self):
        url = reverse("tools_index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('list of tools', str(resp.content))

    def test_tool_page(self):
        url = reverse("tool", args=[self.tool.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(str(self.tool), str(resp.content))
        self.assertIn(str(self.brand), str(resp.content))
        self.assertIn(str(self.section), str(resp.content))

    def test_authorize_page(self):
        url = reverse("authorize_user")

        # Unauthorized users get redirected
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

        # Login and then try again
        self.client.login(username='testadmin', password='foobar')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # Now POST the form, first with no data
        resp = self.client.post(url, data={})
        self.assertEqual(resp.status_code, 200)
        self.assertIn('This field is required.', str(resp.content))

        # Now with data
        resp = self.client.post(url, data={'user_to_authorize': self.user.id, 'authorize_tools': self.tool.id})
        self.assertEqual(resp.status_code, 302)
        self.assertIn(self.tool, self.user.member.authorized_tools.all())
