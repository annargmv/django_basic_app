from django.test import TestCase
from .models import Backend
from fstring import fstring


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Backend.objects.create(title='first todo')
        Backend.objects.create(description='a description here')

    def test_title_content(self):
        back = Backend.objects.get(id=1)
        expected_object_name = fstring("{back.title}")
        self.assertEquals(expected_object_name, 'first todo')

    def test_description_content(self):
        back = Backend.objects.get(id=2)
        expected_object_name = fstring('{back.description}')
        self.assertEquals(expected_object_name, 'a description here')

