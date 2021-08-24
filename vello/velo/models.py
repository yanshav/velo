from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.
class VeloMarsh(models.Model):
    marsh_image = models.FileField(upload_to='images/')
    marsh_text = models.CharField(max_length=300)
    def __str__(self):
        return self.marsh_text

class Quetion(models.Model):
    que_text = models.CharField(max_length=300)
    que_text_raz = models.CharField(max_length=300)

class Marsh(models.Model):
    marsh_name = models.CharField(max_length=100)
    marsh_url_1 = models.URLField()
    marsh_url_2 = models.URLField()
    marsh_text = models.TextField()
    marsh_km = models.CharField(max_length=300)
    marsh_time = models.CharField(max_length=30)
    marsh_obj = models.CharField(max_length=300)
    name = models.ForeignKey(VeloMarsh, on_delete=models.CASCADE, related_name='category', verbose_name="Категория")
    user_mar = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    users_save = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='marsh_liked', blank=True)
