from rest_framework import serializers
from .models import TaskExecution


class TaskExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExecution
        fields = '__all__'
