from django.db import models

class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=50)
    hobby_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.hobby_name}: {self.hobby_description}"


class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length=50)
    portfolio_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.portfolio_name}: {self.portfolio_description}"