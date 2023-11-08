from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
def testing(request):
    """testing static dirs setup correctly"""
    return render(request, "blog/blog.html")

class PostList(generic.ListView):
    model = Post
    context = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 6
    context_object_name = "posts"