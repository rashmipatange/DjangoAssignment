from django.test import TestCase
from phone.models import Phone_number

class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Phone_number.objects.create(name='rashmi', phone_num='9527412635')
        Phone_number.objects.create(name='asmi', phone_num='9642753874')

    def test_name_label(self):
        name_label = Phone_number.objects.get(name='rashmi')
        field_label = name_label._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        name = Phone_number.objects.get(name='rashmi')
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_model_str(self):
        phone_n = Phone_number.objects.get(name='rashmi')
        self.assertEqual(phone_n.__str__(),"rashmi - 9527412635")




