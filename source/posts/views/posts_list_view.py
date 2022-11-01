from django.views.generic import ListView
# from django.db.models import Q
# from urllib.parse import urlencode
# from django.contrib.auth.models import User

# from posts.forms import PostForm
from posts.models import Post


class PostView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ('-created_at',)
    queryset = Post.objects.exclude(is_deleted=True)
    paginate_by = 2
    allow_empty = True
    

    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)
    
    # def get_search_form(self):
    #     return SearchForm(self.request.GET)

    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None

    # def get_queryset(self):
    #     queryset = super().get_queryset().exclude(is_deleted=True)
    #     if self.search_value:
    #         query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
    #         queryset = queryset.filter(query)
    #         if len(queryset) == 0:
    #             return queryset
    #     return queryset
    
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProjectIndexView, self).get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     context['project_users'] =  ProjectUserForm()
    #     if self.search_value:
    #         context['text'] = {'text' : 'Project not found'}
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context