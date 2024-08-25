from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Articles
def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request,'articles/articles.html',{'articles':articles})

def article_details(request,slug):
      # return HttpResponse(slug)
      article = Articles.objects.get(slug=slug)
      return render(request,'articles/article_detail.html',{'article':article})
