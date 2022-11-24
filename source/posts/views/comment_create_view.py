from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect

from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm
from accounts.models import Account


class CommentCreateView (LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post_detail.html'
    
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        print("PRINT1", post, "++++", user)
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return redirect('post_detail', pk=post.pk)
    
    
    # def form_valid(self, form):
    #     post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
    #     user = get_object_or_404(Account, pk=self.kwargs.get('pk'))
    #     form.instance(post=post, user=user)
    #     return super().form_valid(form)
    
    # def get_redirect_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    
    
    # def post(self, request, *args, **kwargs):
    #     print('START')
    #     post = get_object_or_404(Post, pk=kwargs.get('pk'))
    #     # user = get_object_or_404(Account, pk=kwargs.get('pk'))
    #     form = self.get_form_class()(request.POST)
    #     print("request POST ++++", request.POST, "====POST+====",post)
    #     print("PRINT 111", user)
    #     if form.is_valid():
    #         description = form.cleaned_data.get('description')
    #         image = form.cleaned_data.get('image')
    #         author = request.user
    #         # if not Post.objects.filter(description=description).exists():
    #         #     Post.objects.create(description=description, image=image, author=author)
    #     else:
    #         form = {'text' : 'Smth went wrong, post did not create'}
    #     return redirect('post_detail')
    
    
    # def get_success_url(self):
    #     return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    

    
