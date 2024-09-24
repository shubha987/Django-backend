# models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    interests = models.TextField()  # Store interests as comma-separated values
    partner_preferences = models.TextField()  # Store preferences similarly
    event_preferences = models.TextField()  # Store event preferences similarly
