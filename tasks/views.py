from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, DeleteView

# Список всіх задач
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"


# Детальний перегляд задачі
class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"


# Видалення задачі
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    # success_url = 