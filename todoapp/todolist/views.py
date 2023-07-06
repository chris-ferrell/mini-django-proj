from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todo_list": todos})


# post function
@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")

# update function
def update(request, todo_id):
    todo = Todo.object.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

# delete function 
def delete(request, todo_id):
    todo = Todo.object.get(id=todo_id)
    todo.delete()
    return redirect("index")