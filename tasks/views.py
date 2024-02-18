from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Task
from .forms import TaskForm


def index(request: HttpRequest):
    if request.method == "POST":
        data_form = TaskForm(request.POST)
        if data_form.is_valid():
            data_form.save()
        return redirect("/")
    tasks: list[Task] = Task.objects.all()
    form = TaskForm()
    context = {"tasks": tasks, "form": form}
    return render(request, "tasks/list.html", context)
