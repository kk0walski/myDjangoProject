from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.views.generic import ListView, DetailView

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

# Create your views here.
class PostListView(TagMixin, ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    temlate_name = 'blog/post_list.html'
    model = Post

class PostDetail(DetailView):
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'
    model = Post
    slug_field = 'slug'

class TagIndexView(TagMixin, ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        tag = self.kwargs.get('slug')
        return Post.published.filter(tags__slug=self.kwargs.get('slug'))