# projects/models.py

from django.db import models

class Project(models.Model):
    image = models.FileField(upload_to="project_images/", blank=True)