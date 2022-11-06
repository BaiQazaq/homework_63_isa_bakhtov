from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from posts.models import Post
from posts.forms import PostForm


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    model = Post
    
    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        
        if form.is_valid():
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            author = request.user
            if not Post.objects.filter(description=description).exists():
                Post.objects.create(description=description, image=image, author=author)
        else:
            form = {'text' : 'Smth went wrong, post did not create'}
        return redirect('index')
    
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    