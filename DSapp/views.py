from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'message': 'Welcome Home',

        #'time': 'August 27, 2018'
    }
]
def home(request):
    context = {
        'posts': posts
    }

    return render(request,'DSapp/home.html',context)