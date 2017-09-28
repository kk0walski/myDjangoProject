from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class PostsFeed(Feed):
    title = 'Mój blog'
    link ='/blog/'
    description = 'Nowe posty na moim blogu'

    def items(self):
        return Post.published.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)