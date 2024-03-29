from blog.models import *
from sudo.models import Blog


def all(request):
    all_tags = Tag.objects.all()
    all_categories = Categorie.objects.all()
    most_popular_posts = Post.objects.all()[:3]
    random_posts = Post.objects.all()
    recent_post = Post.objects.all().order_by('-date')[:2]
    blog = Blog.objects.get(pk = 1)
    context = {
        'all_tags' : all_tags,
        'all_categories' : all_categories,
        'most_popular_posts' : most_popular_posts,
        'random_posts' : random_posts,
        'recent_posts': recent_post,
        'blog' : blog
    }
    return context