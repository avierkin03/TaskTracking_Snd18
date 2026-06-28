from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path("", views.TaskListView.as_view(), name='task-list'),
    path("task/<int:pk>", views.TaskDetailView.as_view(), name='task-detail'),
    path("delete/<int:pk>", views.TaskDeleteView.as_view(), name='task-delete'),
    path("update/<int:pk>", views.TaskUpdateView.as_view(), name="task-update"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.CustomRegisterView.as_view(), name="register"),
]
