from django.db import models


# Create your models here.

class VeloArticles(models.Model):
    article_image = models.FileField(upload_to='images/')
    article_text = models.TextField()
    article_big_text = models.TextField()
    article_heading = models.CharField(max_length=300)
    article_date = models.DateTimeField()
