from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('username', 'email', 'post', 'message')
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class' : 'form-control'
            })
        }