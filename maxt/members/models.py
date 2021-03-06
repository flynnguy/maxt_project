from django.db import models
from django.contrib.auth.models import User

from tools.models import Tool


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    authorized_tools = models.ManyToManyField(Tool, blank=True)
    rfid_tag_id = models.CharField(max_length=128, blank=True, null=True) # TODO: figure out tag length

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('user',)
