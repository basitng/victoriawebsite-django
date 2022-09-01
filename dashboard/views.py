from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "primary/index.html")


def about(request):
    return render(request, "primary/about.html")


def sermons(request):
    return render(request, "primary/sermons.html")


def ministry(request):
    return render(request, "primary/ministry.html")


def gallery(request):
    return render(request, "primary/gallery.html")


def contact(request):
    return render(request, "primary/contact.html")


def events(request):
    return render(request, "primary/events.html")


def blog(request):
    return render(request, "primary/blog.html")


def blogDetail(request):
    return render(request, "primary/blog-detail.html")


def sermonDetail(request):
    return render(request, "primary/sermon-detail.html")


def eventDetail(request):
    return render(request, "primary/event-detail.html")
