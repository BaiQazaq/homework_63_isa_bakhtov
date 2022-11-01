from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from posts.models import Post
from posts.forms import PostForm



class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse ('post_detail', kwargs={'pk': self.object.pk})

class PostCreate(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    model = Post
    # success_url = 'index'
    
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    