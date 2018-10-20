from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    name = models.CharField(max_length=128)
    trainers = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Tool(models.Model):
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    wiki_link = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.brand != None:
            return " ".join([str(self.brand), self.name])
        return self.name
