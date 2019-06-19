import uuid

from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Good(models.Model):
    unique_name = models.CharField(max_length=200)

    def __str__(self):
        return self.unique_name


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
        return Price.objects.get(id=self.id).good_id.unique_name + '/' + Price.objects.get(
            id=self.id).city_id.name + '/' + str(Price.objects.get(id=self.id).quality)
