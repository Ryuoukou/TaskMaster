from django.db import models
from task_management.models import Task


class TaskExecution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    execution_date = models.DateField(auto_now_add=False, editable=True)

    def __str__(self):
        return f"{self.task.title} - {self.execution_date}"
