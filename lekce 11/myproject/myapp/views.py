from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import MyModel
from .forms import MyModelForm

def index(request):
    my_models = MyModel.objects.filter(user_id=request.user.id)
    return render(request, "index.html", {"my_models": my_models})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/registration.html", {"form": form})

@login_required
def add_item(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Věc byla přidána.")
            return redirect("index")
    else:
        form = MyModelForm()
    return render(request, "add_item.html", {"form": form})
