from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Articles
from django import forms
from django.contrib.auth.decorators import login_required
from .import forms
def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request,'articles/articles.html',{'articles':articles})

def article_details(request,slug):
      # return HttpResponse(slug)
      article = Articles.objects.get(slug=slug)
      return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def create(request): 
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            article = form.save(commit=False)  # Do not save to the database yet
            article.author = request.user
            form.save()
            return redirect("article_list")
    else:       
        form = forms.CreateArticle()
    return render(request,'articles/create_article.html',{'form':form})