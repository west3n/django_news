from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    queryset = Post.objects.all().order_by().values()
    ordering = 'post_date'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
