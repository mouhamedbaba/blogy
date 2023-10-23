from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    date = models.DateField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    partie1 = models.TextField()
    image1_partie1 = models.ImageField(upload_to='media', blank=True)
    image2_partie1 = models.ImageField(upload_to='media', blank=True)
    image3_partie1 = models.ImageField(upload_to='media', blank=True)
    partie2 = models.TextField(blank=True)
    image1_partie2 = models.ImageField(upload_to='media', blank=True)
    image2_partie2 = models.ImageField(upload_to='media', blank=True)
    image3_partie2 = models.ImageField(upload_to='media', blank=True)
    partie3 = models.TextField(blank=True)
    image1_partie3 = models.ImageField(upload_to='media', blank=True)
    image2_partie3 = models.ImageField(upload_to='media', blank=True)
    image3_partie3 = models.ImageField(upload_to='media', blank=True)
    partie4 = models.TextField(blank=True)
    image1_partie4 = models.ImageField(upload_to='media', blank=True)
    image2_partie4 = models.ImageField(upload_to='media', blank=True)
    image3_partie4 = models.ImageField(upload_to='media', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,  blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):

    username = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})

