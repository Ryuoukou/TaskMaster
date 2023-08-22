from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskExecutionViewSet


router = DefaultRouter()
router.register(r'task_executions', TaskExecutionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
