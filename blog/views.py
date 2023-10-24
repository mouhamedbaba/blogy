from django.shortcuts import redirect, render
from blog.forms import CommentForm

from blog.models import Categorie, Comment, Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context ={
        'posts' : posts
    }
    return render(request , 'blog/pages/home.html', context)

def blog(request):
    posts = Post.objects.all()
    context ={
        'posts' : posts
    }
    return render(request, 'blog/pages/blog.html', context)

def single(request, post_id):
    post = Post.objects.get(pk = post_id)
    comments = Comment.objects.filter(post = post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # Enregistrez le post en base de données
            form.save()
            # Redirigez vers une page de confirmation ou ailleurs
            return redirect('blog')
        else :
            print('invalide form')
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments' : comments,
        'form' : form
    }
    return render(request, 'blog/pages/single.html', context)

def categorie(request, cat_name):
    print(f'c name : {cat_name}')
    categorie = Categorie.objects.get(name = cat_name)
    print(categorie)
    posts_categorie_name = Post.objects.filter(categorie = categorie)
    print(posts_categorie_name)
    context = {
        'categorie': categorie,
        'posts_categorie_name' : posts_categorie_name
    }
    return render(request , 'blog/pages/categorie.html', context)


def search(request):
    query = request.GET.get('query')
    print(query)
    posts = Post.objects.filter(title__icontains = query)
    context = {
        'query' : query,
        'result_search' : posts
    }
    return render(request, 'blog/pages/search.html', context)

def contact(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # Enregistrez le post en base de données
            form.save()
            # Redirigez vers une page de confirmation ou ailleurs
            return redirect('contact')
        else :
            print('invalide form')
    else:
        form = CommentForm()
    context = {
        'form' : form
    }
    return render(request , 'blog/pages/contact.html', context)