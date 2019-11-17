from django.db import models
from datetime import datetime
# Create your models here.

class Posts(models.Model):
    title   = models.CharField(max_length=100)
    body    = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.id)+": "+self.title # Parse ID from INT to STR
    class Meta:
        verbose_name_plural = "Posts"