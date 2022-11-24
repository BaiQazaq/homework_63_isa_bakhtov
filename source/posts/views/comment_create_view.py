from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from posts.models import Post, Comment
from posts.forms import CommentForm


class CommentCreateView (LoginRequiredMixin, CreateView):
    form_class = CommentForm
    
    
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        author = self.request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            if not Comment.objects.filter(post=post, author=author, text=text).exists():
                Comment.objects.create(post=post, author=author, text=text)
        else:
            form = {'text' : 'Somthing wrong with comment creation'}
        return redirect('post_detail', pk = post.id)
    
    