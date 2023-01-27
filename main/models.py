from django.db import models

class Source(models.Model):
    url = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=30, null=True)

class Data(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
