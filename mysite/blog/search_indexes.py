from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr="author")
    publish = indexes.DateTimeField(model_attr="publish")
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().published.all()