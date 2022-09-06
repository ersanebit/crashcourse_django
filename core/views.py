from http.client import HTTPResponse
from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/frontpage.html',{'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "DIsallow: /admin/",
    ]
    return HTTPResponse("\n".join(text), content_type="text/plain")

