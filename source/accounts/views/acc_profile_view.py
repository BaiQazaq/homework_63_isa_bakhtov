from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DetailView


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    # paginate_related_by = 5
    # paginate_related_orphans = 0

    # def get_context_data(self, **kwargs):
    #     articles = self.object.articles.order_by('-created_at')
    #     paginator = Paginator(articles, self.paginate_related_by, orphans=self.paginate_related_orphans)
    #     page_number = self.request.GET.get('page', 1)
    #     page = paginator.get_page(page_number)
    #     kwargs['page_obj'] = page
    #     kwargs['articles'] = page.object_list
    #     kwargs['is_paginated'] = page.has_other_pages()
    #     return super().get_context_data(**kwargs)
