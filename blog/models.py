# blog/models.py
from django.db import models

class PublicManager(models.Manager):
	def get_queryset(self):
		return super(PublicManager,
			self).get_queryset()\
		.filter(status="public")

	def title_count(self, keyword): # NEW
		return self.filter(title__icontains=keyword).count()

class Post(models.Model):
	STATUS_CHOICES = (
		('public','Public'),
		('private','Private')
	)

	title = models.CharField(max_length=100)
	content = models.TextField()
	status = models.CharField(
		max_length=10,
		choices = STATUS_CHOICES,
		default = 'public'
	)

	objects = models.Manager()
	public = PublicManager()

	def __str__(self):
		return self.title