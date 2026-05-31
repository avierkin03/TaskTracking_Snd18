from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path("", views.TaskListView.as_view(), name='task-list'),
    path("task/<int:pk>", views.TaskDetailView.as_view(), name='task-detail'),
    path("delete/<int:pk>", views.TaskDeleteView.as_view(), name='task-delete'),
]
