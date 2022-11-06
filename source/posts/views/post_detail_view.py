from django.views.generic import DetailView

from posts.models import Post


class ProjectView(DetailView):
    template_name = 'post_detail.html'
    model =  Post
    pk_url_kwarg = 'pk'