from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from .models import Blog, Blogger, Comment
from .forms import AddCommentForm, AddBlogForm


class BlogsListView(ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog


class BloggersListView(ListView):
    model = Blogger


class BloggerDetailView(DetailView):
    model = Blogger


def index(request):
    return render(request, 'index.html')


@login_required
def add_comment(request, pk):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.get(pk=pk)
            author = request.user.blogger
            comment = Comment.objects.create(
                blog=blog,
                author=author,
                content=form.cleaned_data['content'],
            )
            return HttpResponseRedirect(blog.get_absolute_url())
    else:
        form = AddCommentForm()

    return render(request, 'blog/add_comment.html', {'form': form})


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST)
        if form.is_valid():
            author = request.user.blogger
            blog = Blog.objects.create(
                name=form.cleaned_data['name'],
                author=author,
                content=form.cleaned_data['content'],
            )
            return HttpResponseRedirect(blog.get_absolute_url())
    else:
        form = AddBlogForm()

    return render(request, 'blog/add_blog.html', {'form': form})
