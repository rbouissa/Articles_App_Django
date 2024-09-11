from django.urls import path
from . import views
from articles import views as views_article
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views_article.article_list,name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

urlpatterns += staticfiles_urlpatterns()