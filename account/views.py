from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'login.html')


def start_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/events')
    return render(request, 'start_page.html')
