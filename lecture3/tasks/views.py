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
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
