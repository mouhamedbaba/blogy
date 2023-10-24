from django import forms
from django.contrib.auth.models import User
from blog.models import Post


# class CommentForm(forms.ModelForm):
    
#     class Meta:
#         model = Comment
#         fields = ('username', 'email', 'post', 'message')
#         widgets = {
#             'username' : forms.TextInput(attrs={
#                 'class' : 'form-control'
#             }),
#             'email' : forms.EmailInput(attrs={
#                 'class' : 'form-control'
#             }),
#             'message': forms.Textarea(attrs={
#                 'class' : 'form-control'
#             })
#         }
    
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        # fields = ("title",'image','author', 'partie1')
        fields = ("title",'image','author', 'partie1', 'image1_partie1', 'image2_partie1','image3_partie1','partie2', 'image1_partie2', 'image2_partie2','image3_partie2', 'partie3', 'image1_partie3', 'image2_partie3', 'image3_partie3', 'partie4', 'image1_partie4', 'image2_partie4','image3_partie4','tags', 'categorie')