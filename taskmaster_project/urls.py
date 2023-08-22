from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_management/', include('task_management.urls')),
    path('data_analytics/', include('data_analytics.urls')),
    path('accounts/', include('accounts.urls')),
]
