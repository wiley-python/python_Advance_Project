from django.db import models


class flightDetails:
    objects = models.Manager()
    flightNo = models.IntegerField(max_length=4)
    date = models.DateField()
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    capacity = models.IntegerField()
    cost = models.FloatField()

    class Meta:
        db_table = 'flight'
