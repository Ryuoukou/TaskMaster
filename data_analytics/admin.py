from django.contrib import admin
from .models import TaskExecution


class TaskExecutionAdmin(admin.ModelAdmin):
    list_display = ('task', 'execution_date')


admin.site.register(TaskExecution, TaskExecutionAdmin)
