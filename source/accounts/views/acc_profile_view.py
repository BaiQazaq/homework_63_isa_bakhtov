from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.views.generic import  DetailView
from posts.models import Post
from accounts.forms import SubsForm



class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self,object_list=None, **kwargs):
        context = super(ProfileView, self).get_context_data(object_list=object_list, **kwargs)
        author = self.get_object()
        posts = Post.objects.filter(author=author).order_by('-created_at')
        context['subscription_form'] = SubsForm()
        # subs = Subs.objects.filter(subs_by=author).order_by('-subs_by')
        paginator = Paginator(posts, self.paginate_related_by, orphans=self.paginate_related_orphans)
        # paginator = Paginator(subs, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['posts'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs, context=context)

