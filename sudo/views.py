from django.shortcuts import render

from blog.models import *

# Create your views here.

def home(request):
    return render(request, 'sudo/pages/home.html')

def contact(request):
    contacts = Contact.objects.all().order_by('-date')
    context = {
        'contacts' : contacts
    }
    return render(request, 'sudo/pages/contact.html', context)

def messages(request):
    messages = Message.objects.all().order_by('-date')
    context = {
        'messages' : messages
    }
    return render(request, 'sudo/pages/messages.html', context)