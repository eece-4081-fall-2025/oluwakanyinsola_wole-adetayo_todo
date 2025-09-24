from django.shortcuts import render
from .models import Todo

def index(request):
    todos = Todo.objects.order_by('-created_at') if hasattr(Todo, 'objects') else []
    return render(request, "five/index.html", {"todos": todos})
