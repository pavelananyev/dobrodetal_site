from django.db import models


def photos_directory(instance, filename):
    return f'/photos/{instance.article}/{filename}'


class Detail(models.Model):
    title = models.CharField(max_length=255)
    article = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to=photos_directory)
    description = models.TextField()
    price = models.PositiveIntegerField()
    second_price = models.PositiveIntegerField(blank=True)
    available = models.BooleanField(default=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
