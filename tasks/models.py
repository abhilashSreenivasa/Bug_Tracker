from django.contrib.auth.models import User
from django.db import models


class TaskCategory(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.category


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
