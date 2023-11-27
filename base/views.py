from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(
                request, "There was an error in your submission. Please check the form."
            )
    else:
        form = ContactForm()

    return render(request, "base/home.html", {"form": form})


def about(request):
    return render(request, "base/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(
                request, "There was an error in your submission. Please check the form."
            )
    else:
        form = ContactForm()

    return render(request, "base/contact.html", {"form": form})
