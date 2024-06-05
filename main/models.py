from django.db import models

class Source(models.Model):
    url = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

class Data(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=255, null=True)

class Resources(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.CharField(max_length=50)
    # data_new = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    region_code = models.IntegerField()
    region_source = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    url = models.CharField(max_length=256)
    category = models.CharField(max_length=50)
    item_title_original = models.CharField(max_length=50)
    item_title_ru = models.CharField(max_length=50)
    article_title_original = models.CharField(max_length=50)
    filter = models.IntegerField()
