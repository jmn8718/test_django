from __future__ import unicode_literals

from django.db import models

class App(models.Model):
	ACCESS_RIGHTS = (
	    ('PU','Public'),
	    ('PR','Private'),
	)
	file = models.FileField(upload_to='uploads/')
	description = models.TextField()
	link = models.URLField(max_length=200)
	access_right= models.CharField(max_length=2, choices=ACCESS_RIGHTS)
