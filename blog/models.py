from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) # 길이 제한이 있음
    content = models.TextField()

    created = models.DateTimeField()
    author = models.ForeignKey(User)