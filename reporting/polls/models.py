from django.db import models
from django.utils import timezone

# Create your models here.

class Report(models.Model):
	report_text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.report_text
	def is_recent(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
	report = models.ForeignKey(Report, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date added')
	def __str__(self):
		return self.comment_text