from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class GeoBlocker(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    restriction = GenericRelation(GeoBlocker, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    restriction = GenericRelation(GeoBlocker, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Trailer(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    restriction = GenericRelation(GeoBlocker, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
