from django.urls import path
from .views import PostsList, PostDetail, search, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search', search),
   path('add/', PostCreateView.as_view(), name='post_create'),
   path('<int:pk>/edit', PostUpdateView.as_view(), name='product_update'),
   path('<int:pk>/delete', PostDeleteView.as_view(), name='product_delete'),
]