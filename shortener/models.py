from django.db import models
from django.conf import settings
from .utils import create_shortcode

# Create your models here.

SHORTCODE_MAX = getattr('settings', 'SHORTCODE_MAX', 10)

class myURLShManager(models.Manager):

	"""
	override the default all method in the model manager
	"""

	def all(self, *args, **kwargs):
		qs = super(myURLShManager, self).all(*args, **kwargs)
		qs = qs.filter(active=True)
		return qs


	"""
	get all shortcodes and refresh them
	"""

	def refresh_shortcodes(self, items=None):
		qs = myURLSh.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs =  qs.order_by("-id")[:items]
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save
			new_codes +=1

		return 'New codes made: {i}'.format(i=new_codes)

class myURLSh(models.Model):
	url         = models.CharField(max_length=220, )
	shortcode 	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	active 		= models.BooleanField(default=True)

	"""
	below line overrides the default model manager.
	"""
	objects = myURLShManager()

	def save(self, *args, **kwargs):
		if not self.shortcode:
			self.shortcode = create_shortcode(self)
		super(myURLSh, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)