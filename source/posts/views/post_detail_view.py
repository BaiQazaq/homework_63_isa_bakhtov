from django.views.generic import DetailView
from urllib.parse import urlencode

from posts.models import Post
from posts.forms import CommentForm

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model =  Post
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['comment_form'] = CommentForm()
        # context['subscription_form'] = SubsForm()
        post = self.object
        comments = post.comments.order_by('author')
        context['comments'] = comments
        return context
    
    