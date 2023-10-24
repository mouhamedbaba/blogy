from django.shortcuts import render

# Create your views here.

def login_admin(request):
    return render(request, 'authentication/admin/login.html')