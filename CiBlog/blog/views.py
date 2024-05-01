from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from .models import Post
from .forms import CommentForm

# Create your views here.
def testing(request):
    """testing static dirs setup correctly"""
    return render(request, "blog/blog.html")

class PostList(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(status=1).order_by("-created_on")
        context = {"posts": queryset}
        print(context)
        return render(request, "blog/blog.html", context)
    

class PostDetail(View):
    def get(self, request, postSlug,*args, **kwargs, ):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug = postSlug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        comment_form = None
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {"post": post,
                   "comments": comments,
                   "liked": liked,
                   "commented": False,
                   "comment_form": CommentForm}
        return render(request, "blog/blogDetails.html", context)
    
    def post(self, request, postSlug,*args, **kwargs, ):
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug = postSlug)
            comments = post.comments.filter(approved=True).order_by("created_on")
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                comment_form=CommentForm()
            context = {"post": post,
                    "comments": comments,
                    "liked": liked,
                    "commented": True,
                    "comment_form": CommentForm}
           
            return HttpResponseRedirect(self.request.path_info)


def testingView(request):
    context = {"request": request}
    print("2")
    print("3")
    return render(request, "blog/testing.html", context)