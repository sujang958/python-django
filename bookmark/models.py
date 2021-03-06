from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=100, null=True);
    url = models.URLField('url', unique=True);

    def __str__(self):
        return self.title;