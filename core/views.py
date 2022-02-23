from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpFrom

# Create your views here.


def frontpage(request):
    return render(request, "core/frontpage.html")


def signup(request):
    if request.method == "POST":
        form = SignUpFrom(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("frontpage")

    else:
        form = SignUpFrom()
    return render(request, "core/signup.html", {"form": form})
