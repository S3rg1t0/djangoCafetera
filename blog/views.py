from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request=request,
                  template_name="blog/blog.html",
                  context={"posts": posts})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    print(category.get_posts.all())
    return render(request=request,
                  template_name="blog/category.html",
                  context={"category": category})




