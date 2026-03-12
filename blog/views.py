from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from .models import Post, Tag
from .forms import CreatePostForm, CommentForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-create_time')
    tags = Tag.objects.all()
    #this line is for us to get the specific tag in url, like /?tag=Python
    tag_name = request.GET.get('tag')
    if tag_name:
        posts = posts.filter(tags__tag_name=tag_name)
    query = request.GET.get('query')
    if query:
        posts = posts.filter(title__icontains=query)
    context = {'posts': posts, 'tags': tags}
    return render(request, 'blog/post_list.html', context= context)
