from django.db import models

class Road(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

class RoadProperties(models.Model):
    length = models.DecimalField(max_digits=19, decimal_places=10)
    width = models.DecimalField(max_digits=19, decimal_places=10)
    latitude = models.DecimalField(max_digits=19, decimal_places=10)
    longitude = models.DecimalField(max_digits=19, decimal_places=10)
    road_type = models.CharField(max_length=250, blank=False, null=False)
    name_id = models.ForeignKey(
        Road, on_delete=models.CASCADE, null=True,blank=False)


