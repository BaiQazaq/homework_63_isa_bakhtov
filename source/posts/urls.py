from django.urls import path

from posts.views.post_create_view import PostCreate
from posts.views.posts_list_view import PostView

urlpatterns = [
    path("", PostView.as_view(), name='index'),
    path("add/", PostCreate.as_view(), name='post_creation'),
    path("detail/", PostCreate.as_view(), name='post_detail'),
    
]