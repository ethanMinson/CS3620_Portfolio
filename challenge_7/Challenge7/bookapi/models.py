from django.db import models

# Create your models here.
class BookData(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(blank=True, default='default.jpg')

    def __str__(self):
        return self.title