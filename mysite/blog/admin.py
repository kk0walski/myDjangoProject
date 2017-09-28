from django import forms
from django.contrib import admin
from .models import Post
from taggit_labels.widgets import LabelWidget
from taggit.forms import TagField
# Register your models here.

class ContentForm(forms.ModelForm):
    tags = TagField(required=False, widget=LabelWidget)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'tag_list')
    list_filter = ('status', 'created', 'publish', 'author', 'tags')
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    form = ContentForm

    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(Post, PostAdmin)