from django_filters import FilterSet, DateFromToRangeFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author, Category
from django import forms


class PostFilter(FilterSet):
    date = DateFromToRangeFilter(field_name='creationTime', widget=forms.SplitDateTimeWidget(
            attrs={
                'type': 'date'
            }
        ),
                                 lookup_expr='gt', label='Creation date')
    title = CharFilter(field_name='head', lookup_expr='icontains', label='Title')
    author = CharFilter(field_name='postAuthor__authorAccount__username', lookup_expr='icontains', label="Author")
    category = ModelChoiceFilter(field_name='postCategory__name', queryset=Category.objects.all(), label="Category")

    class Meta:
        model = Post
        fields = ['author', 'title', 'category', 'date']
