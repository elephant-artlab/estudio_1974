import os

from django.db import models
from django.db.models.signals import pre_delete

# Create your models here.
class Session(models.Model):
	title = models.CharField(max_length=17, null=False, blank=False)
	subtitle = models.CharField(max_length=29, null=False, blank=False)
	video_url = models.URLField(blank=True, null=True)
	image = models.ImageField(upload_to="uploads", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	#Displays objects "title" in the admin instead of "Project object"
	def __unicode__(self):
		return unicode(self.title)

def clean_photos(sender, instance, **kwargs):
	if instance.image:
		if os.path.isfile(instance.image.path):
			os.remove(instance.image.path)

pre_delete.connect(clean_photos, sender=Session)