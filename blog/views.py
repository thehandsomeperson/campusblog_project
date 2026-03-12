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

#only the person logged in can create posts
@login_required
def create_post(request):
    if request.method == 'POST':
        # user submit the form and put data into CreatePostForm
        form = CreatePostForm(request.POST)
        if form.is_valid():
            #after proof passed, we got the post but not save here
            post = form.save(commit=False)
            #the author is the person who has already logged in
            post.author = request.user
            if 'save_draft' in request.POST:
                post.status = 'draft'
            else:
                post.status = 'published'
            post.save()
            #manually save m2m relations (Tags) when using commit=False
            form.save_m2m()
            #get value of new_tags from form
            new_tags = form.cleaned_data['new_tags']
            components = new_tags.split(',')
            tag_list = []
            for tag in components:
                if tag.strip() != '':
                    tag_list.append(tag.strip())
            for tag_name in tag_list:
                #find or create tag by tag_name
                tag, created = Tag.objects.get_or_create(tag_name=tag_name)
                #associate tag object to post
                post.tags.add(tag)
            #redirect to post_list page
            return redirect('blog:post_list')
    else:
        # When user open the page, give them an empty page
        form = CreatePostForm()

    # GET or POST failure，then render the create_post page again
    return render(request, 'blog/create_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'blog/post_detail.html', context=context)

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("You have no rights to edit this post.")
    if request.method == 'POST':
        # user make change on the original form
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            #after proof passed, we got the post but not save here
            post = form.save(commit=False)
            #the author is the person who has already logged in
            post.author = request.user
            if 'save_draft' in request.POST:
                post.status = 'draft'
            else:
                post.status = 'published'
            post.save()
            form.save_m2m()
            new_tags = form.cleaned_data['new_tags']
            components = new_tags.split(',')
            tag_list = []
            for tag in components:
                if tag.strip() != '':
                    tag_list.append(tag.strip())
            for tag_name in tag_list:
                # find or create tag by tag_name
                tag, created = Tag.objects.get_or_create(tag_name=tag_name)
                # associate tag object to post
                post.tags.add(tag)
            #redirect to post_detail page
            return redirect('blog:post_detail', post_id=post_id)
    else:
        # When user open the page, give them the original form which contains information before
        form = CreatePostForm(instance=post)

    # GET or POST failure，then render the create_post page again
    return render(request, 'blog/edit_post.html', {'form': form})
