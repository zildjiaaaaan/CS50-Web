from django import forms
from django.http import HttpResponse
from django.shortcuts import render

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

tasks = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

# Add a new task:
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
