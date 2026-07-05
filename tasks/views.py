from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import TaskFilterForm, TaskCreateForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Список всіх задач
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")
        owner = self.request.GET.get("owner")

        if status:
            queryset = queryset.filter(status = status)
        if priority:
            queryset = queryset.filter(priority = priority)
        if owner:
            queryset = queryset.filter(owner = owner)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm()
        return context


# Створення нової задачі
class TaskCraeteView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("tasks:task-list")


# Детальний перегляд задачі
class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"


# Видалення задачі
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks:task-list")


# Створення задачі
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("tasks:task-list")


# Редагування задачі
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "tasks/task_update.html"
    success_url = reverse_lazy("tasks:task-list")


# Логаут
class CustomLogoutView(LogoutView):
    next_page = 'tasks:task-list'


# Логін
class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True


# Реєстрація
class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "auth/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("tasks:task-list"))