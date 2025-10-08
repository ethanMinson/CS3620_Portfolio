from django.db import models

# Create your models here.
class Madlib(models.Model):
    title = models.CharField(max_length=100)
    blanks = models.JSONField(default=list)
    story_clips = models.JSONField(default=list)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class FinishedStory(models.Model):
    title = models.CharField(max_length=100)
    answers = models.JSONField(default=list)

    def __str__(self):
        return self.title