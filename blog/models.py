from django.db import models
# we just use the User model form auth.models
from django.contrib.auth.models import User

# Create your models here.
# Create Tag table
class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_name

#Create Post table
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    # in this step, it is a matched from database to Admin
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'), ]
    #used for regular users can only choose from these two options
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#create Comment table
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} on '{self.blog_post.title}'"





