from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Neighbourhood,Posts,Business
from django.contrib.auth.decorators import login_required.

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    posts=Posts.show_posts()
    return render(request, 'hood/home.html',{'posts':posts})



@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'hood/search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'hood/search.html',{"message":message})