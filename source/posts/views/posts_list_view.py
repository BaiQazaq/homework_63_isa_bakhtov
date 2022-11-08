from django.views.generic import ListView
from django.db.models import Q
from urllib.parse import urlencode
# from django.contrib.auth.models import User

from posts.forms import SearchForm
from posts.models import Comment, Post
from accounts.models import Account


class PostView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ('-created_at',)
    queryset = Post.objects.exclude(is_deleted=True)
    paginate_by = 2
    allow_empty = True
    

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)
    
    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        # print("PRINT111", queryset)
        if self.search_value:
            users = Account.objects.all()
            # print("PRINT222", users)
            query = Q(email__icontains=self.search_value) | Q(last_name__icontains=self.search_value) | Q(first_name__icontains=self.search_value) | Q(username__icontains=self.search_value)
            users_got = users.filter(query)
            user = users_got.values('id')[0]
            # print("PRINT333", user['id'])
            id = int(user['id'])
            queryset = queryset.filter(author_id=id)
            # print("PRIN444",queryset)
            if len(queryset) == 0:
                return queryset
        return queryset
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostView, self).get_context_data(object_list=object_list, **kwargs)
        # print("PRINT555", context)
        posts = self.get_queryset().exclude(is_deleted=True)
        posts_id = posts.values('id')
        # print("PRINT666", posts_id)
        comments = []
        for i in posts_id:
            # print("i"*10, i)
            id = int(i['id'])
            # print("POST777", id)
            comments.append(Comment.objects.filter(post_id=id))
            # print("PRINT999", comments)
            kwargs['comments'] = comments
        context['form'] = self.form
        #context['project_users'] =  ProjectUserForm()
        if self.search_value:
            context['text'] = {'text' : 'Project not found'}
            context['query'] = urlencode({'search': self.search_value})
        return context