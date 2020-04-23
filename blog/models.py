from django.db import models


class User(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)


class Post(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    body = models.TextField()
