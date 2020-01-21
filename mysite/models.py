from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    edited_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
