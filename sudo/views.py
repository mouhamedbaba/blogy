from django.shortcuts import redirect, render

from blog.models import *

from sudo.forms import *

# Create your views here.

def home(request):
    return render(request, 'sudo/pages/home.html')

def post(request):
    if request.method == 'POST' :
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else :
        form = PostForm()
    context = {
        'titre_page' : 'Creer une article',
        'form' : form
    }
    return render(request , 'sudo/pages/post.html', context)

def contact(request):
    contacts = Contact.objects.all().order_by('-date')
    context = {
        'contacts' : contacts,
        'titre_page' : 'Contacts'
    }
    return render(request, 'sudo/pages/contact.html', context)

def messages(request):
    messages = Message.objects.all().order_by('-date')
    context = {
        'messages' : messages,
        'titre_page' : 'Messages'
    }
    return render(request, 'sudo/pages/messages.html', context)

def authors(request):
    context = {
        'titre_page' : 'Auteurs des articles'
    }
    return render(request, 'sudo/pages/authors.html', context)