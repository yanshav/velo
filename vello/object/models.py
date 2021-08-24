from django.db import models

# Create your models here.
class VeloObject(models.Model):
	object_image = models.FileField(upload_to='images/')
	object_image_map = models.FileField(upload_to='images/')
	object_heading = models.CharField(max_length=300)
	object_text = models.TextField()
	object_big_text = models.TextField()
	object_addr=models.CharField(max_length=300)
	object_phone=models.CharField(max_length=30)
	object_email=models.EmailField()
