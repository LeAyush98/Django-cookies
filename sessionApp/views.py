from django.shortcuts import render, redirect
from django.http import HttpResponse
from sessionApp.forms import ItemsForm
from django.urls import reverse
# Create your views here.

def home(request):
    if "count" in request.COOKIES:
        count = int(request.COOKIES["count"]) + 1
    else: count = 1     
    response = render(request, "sessionApp/index.html", {"count":count})
    response.set_cookie("count", count)
    return response

def add(request):
    form = ItemsForm()
    response = render(request, "sessionApp/add.html", {"form": form})
    if request.method == "GET":
        return response
    elif request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            quantity = form.cleaned_data["quantity"]
            response.set_cookie(item,quantity)
        return response

def display(request):
    return render(request, "sessionApp/display.html")