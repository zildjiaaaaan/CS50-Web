from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")    

def greet(request, name):
    # return HttpResponse(f"Hello, {name}")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    