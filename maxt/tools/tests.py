from django.test import TestCase
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

