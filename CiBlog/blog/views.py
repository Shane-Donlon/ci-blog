from django.shortcuts import render

# Create your views here.
def testing(request):
    """testing static dirs setup correctly"""
    return render(request, "blog/blog.html")