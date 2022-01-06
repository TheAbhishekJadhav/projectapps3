from django.db import models

# Create your models here.
class Assets(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Bookings(models.Model):
    asset = models.ManyToManyField(Assets)
    user = models.CharField(max_length=100)
    time_block = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
