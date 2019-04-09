from django.db import models

class PublicManager(models.Manager):
	def get_queryset(self):
		return super(PublicManager,
			self).get_queryset()\
		.filter(status="public")

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

	objects = Manager()
	public = PublicManager()

	def __str__(self):
		return self.title