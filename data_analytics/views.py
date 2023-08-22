from rest_framework import viewsets
from .models import TaskExecution
from .serializers import TaskExecutionSerializer


class TaskExecutionViewSet(viewsets.ModelViewSet):
    queryset = TaskExecution.objects.all()
    serializer_class = TaskExecutionSerializer
