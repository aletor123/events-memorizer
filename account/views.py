from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'login.html')


def start_page(request):
    return render(request, 'start_page.html')
