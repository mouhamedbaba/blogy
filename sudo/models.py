from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):

    name = models.CharField(max_length=50)
    dark_logo = models.FileField(upload_to='media', null=True)
    logo = models.ImageField(upload_to='media')
    default_avatar = models.ImageField(upload_to='media')
    favicon = models.ImageField(upload_to='media', blank=True, null=True)
    email = models.EmailField(max_length=254)
    telephone = models.IntegerField()
    localisation = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})

