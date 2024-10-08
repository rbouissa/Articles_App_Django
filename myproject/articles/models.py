from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='defaault_image.png',blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Add on_delete

#to let what the value of the object inside the shell that we used to let the datatbse intract with our app (ORM)\
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'...'