from gc import get_objects
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm
from .models import Post, Tag

def detail(request, tag_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})

def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    return render(request, 'blog/tag.html', {'tag': tag})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(title_icontains=query)

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})