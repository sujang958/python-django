from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    description = models.CharField('Description', max_length=100, help_text='description!', blank=True)

    def __str__(self):
        return self.title