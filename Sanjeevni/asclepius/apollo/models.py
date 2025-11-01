from django.db import models

class Report(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    symptoms = models.JSONField(default=list)  # stores ["fever", "cough"]
    created_at = models.DateTimeField(auto_now_add=True)
