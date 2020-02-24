from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Neighbourhood,Posts,Business

# Create your views here.
def home(request):
    posts=Posts.show_posts()
    return render(request, 'hood/home.html',{'posts':posts})