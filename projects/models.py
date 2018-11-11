from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=454)
    summary = models.CharField(max_length=454)
    pending_tasks = models.CharField(max_length=454)
    progress_made = models.CharField(max_length=454)
    additional_info = models.CharField(max_length=454)
    slack_channel = models.CharField(max_length=200)
