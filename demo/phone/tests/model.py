from django.test import TestCase
from phone.models import Phone_number

class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Phone_number.objects.create(name='rashmi', phone_num='9527412635')

    def test_name_label(self):
        name_label = Phone_number.objects.get(name='rashmi')
        field_label = name_label._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        name = Phone_number.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_model_str(self):
        phone_n = Phone_number.objects.get(name='rashmi')
        expected_object= f'{phone_n.name}, {phone_n.phone_num}'
        self.assertEqual(str(phone_n), expected_object)




