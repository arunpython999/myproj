from django.db import models


# Create your models here.
class Theatre(models.Model):
    name = models.CharField(max_length=100, null=True)
    no_of_seats = models.IntegerField(null=True)
    ac = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=100, null=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

