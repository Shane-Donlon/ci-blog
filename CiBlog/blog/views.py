from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
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
    

class PostDetails(DetailView):
    model = Post
    pk_url_kwarg = "postPk"
    template_name = "blog/blogDetails.html"
    context_object_name = "posts"
    