from django.forms import *
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['postAuthor', 'postCategory', 'nameCategory', 'head', 'text']
