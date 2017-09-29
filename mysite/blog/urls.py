from django.conf.urls import url
from . import views
from .views import TagIndexView, PostDetail, PostSearch
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from .feeds import PostsFeed

sitemaps = {
    'posts' : PostSitemap
}

urlpatterns = [
    # Widoki posta
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<slug>[-\w]+)/$',
        PostDetail.as_view(),
        name='post_detail'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps' : sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^feed/$', PostsFeed(), name='post_feed'),
    url(r'^search/$', PostSearch.as_view(), name='post_search')
]