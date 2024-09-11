from django.urls import path
from . import views
#app_name = 'article'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/',views.create,name='create'),
    path('<slug:slug>/',views.article_details,name='article_details'),
]
