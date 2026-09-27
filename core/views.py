from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def robots_txt(request):
    content = (settings.BASE_DIR / "robots.txt").read_text(encoding="utf-8")
    return HttpResponse(content, content_type="text/plain")