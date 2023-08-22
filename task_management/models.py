from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.CharField(max_length=20, choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")])
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[("todo", "To Do"), ("in_progress", "In Progress"), ("done", "Done")])

    def __str__(self):
        return self.title
