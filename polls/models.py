import uuid

from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Good(models.Model):
    localization_name_variable = models.CharField(max_length=200)
    localization_description_variable = models.CharField(max_length=200)
    index = models.IntegerField()
    unique_name = models.CharField(max_length=200)

    def __str__(self):
        return self.unique_name

    @staticmethod
    def convert_json_to_good(json_data: str):
        prices = []  # type:[Price]
        return prices

    @staticmethod
    def update_good(goods: []):
        is_succeeded = False
        return is_succeeded


class Price(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    good_id = models.ForeignKey(Good, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    quality = models.PositiveSmallIntegerField()
    sell_price_min = models.BigIntegerField()
    sell_price_min_date = models.DateTimeField()
    sell_price_max = models.BigIntegerField()
    sell_price_max_date = models.DateTimeField()
    buy_price_min = models.BigIntegerField()
    buy_price_min_date = models.DateTimeField()
    buy_price_max = models.BigIntegerField()
    buy_price_max_date = models.DateTimeField()

    def __str__(self):
        name = Price.objects.get(id=self.id).good_id.unique_name
        city = Price.objects.get(id=self.id).city_id.name
        tier = str(Price.objects.get(id=self.id).quality)
        return name + '/' + city + '/' + tier

    @staticmethod
    def convert_json_to_price(json_data: str):
        prices = []  # type:[Price]
        return prices

    @staticmethod
    def update_price(prices: []):
        is_succeeded = False
        return is_succeeded
