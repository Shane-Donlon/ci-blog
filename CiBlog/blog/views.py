from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
from .models import Post

# Create your views here.
def testing(request):
    """testing static dirs setup correctly"""
    return render(request, "blog/blog.html")

class PostList(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(status=1).order_by("-created_on")
        context = {"posts": queryset}
        return render(request, "blog/blog.html", context)
    

class PostDetail(View):
    def get(self, request, postSlug,*args, **kwargs, ):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug = postSlug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {"post": post,
                   "comments": comments,
                   "liked": liked}
        return render(request, "blog/blogDetails.html", context)
    