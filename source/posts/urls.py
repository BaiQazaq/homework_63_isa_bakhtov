from django.urls import path

from posts.views.post_create_view import PostCreate
from posts.views.posts_list_view import PostView
from posts.views.post_detail_view import PostDetailView
from posts.views.comment_create_view import CommentCreateView
from posts.views.like_add import LikeAddView

urlpatterns = [
    path("", PostView.as_view(), name='index'),
    path("add/", PostCreate.as_view(), name='post_creation'),
    path("detail/<int:pk>", PostDetailView.as_view(), name='post_detail'),
    
    path("detail/<int:pk>/comment/add/", CommentCreateView.as_view(), name="comment_add"),
    path("detail/<int:pk>/like/add/", LikeAddView.as_view(), name="like_add")
    
]