from django.db.models import Q
from gc import get_objects

from django.shortcuts import get_object_or_404, render, redirect
from .forms import BlogForm, CommentForm
from .models import Post, Tag

def detail(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', id=id)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})

def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    return render(request, 'blog/tag.html', {'tag': tag})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

def add(request):
    return render(request, 'blog/add.html', { 'BlogForm': BlogForm})

def create(request):
    form = BlogForm(request.POST)
    obj = form.save(commit=False)
    obj.slug = 'text' 
    obj.save()
    # if form.is_valid():
    #     try:
    #         return redirect('/')
    #     except:
    #         pass

    return redirect( '/')

def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')
