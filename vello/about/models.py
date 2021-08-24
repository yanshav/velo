from django.db import models

# Create your models here.

class About_main(models.Model):
	about_main_image = models.FileField(upload_to='images/')
	about_main_text = models.CharField(max_length=30)
	about_main_description = models.TextField()

class About_one(models.Model):
	about_one_text = models.CharField(max_length=30)
	about_one_title = models.TextField()
	about_one_description = models.TextField()
	about_one_end = models.TextField()

class About_partners(models.Model):
	about_partners_image = models.FileField(upload_to='images/')

