from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Todo

def index(request):
    todos = Todo.objects.order_by('-created_at')
    return render(request, "five/index.html", {"todos": todos})


def task_create(request):
    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        if title:
            Todo.objects.create(title=title)  # minimal fields for the test
        return redirect("five:index")
    # If someone hits GET on /create/, just bounce back to index
    return redirect("five:index")

def task_edit(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        if title:
            task.title = title
            task.save()
        return redirect("five:index")
    return redirect("five:index")


def task_delete(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        task.delete()
    return redirect("five:index")

def task_toggle(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("five:index")

def task_move(request, pk, direction):
    # Stub: just validate & redirect; ordering logic comes later
    get_object_or_404(Todo, pk=pk)
    if direction not in ("up", "down"):
        return HttpResponseBadRequest("Invalid direction")
    return redirect("five:index")
