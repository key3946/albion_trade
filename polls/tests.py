from django.contrib.staticfiles.templatetags.staticfiles import static
from django.test import TestCase


# Create your tests here.
from polls.models import Good


class CityModelTests(TestCase):
    def テスト項目1(self):
        return self.assertIs(True, True)


class GoodModelTests(TestCase):
    def 正しいJsonDataでGoodオブジェクトに変換できる(self):
        with open(static('polls/test/model/good/goods.json')) as json_file:
            json_data_str = json_file.read()
        good_objects = Good.convert_json_to_good(json_data_str)

        expect = []
        return self.assertEqual(True, True)

    def GoodオブジェクトをDBに挿入できる(self):

        return self.assertEqual()


class PriceModelTests(TestCase):
    def テスト項目1(self):
        return self.assertIs(True, True)


