from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done")
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("hight", "Hight")
    ]

    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    deadline = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="tasks")

    def __str__(self):
        return self.title
