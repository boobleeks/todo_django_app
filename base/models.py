from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    complete = models.BooleanField(default = False)
    create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        ordering = ["complete"]
