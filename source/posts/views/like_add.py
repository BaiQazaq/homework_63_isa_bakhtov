from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# import json
# from django.http import HttpResponse
from django.views.generic import CreateView
from posts.models import Like, Post
from posts.forms import LikeForm




class LikeAddView(LoginRequiredMixin, CreateView):
    form_class = LikeForm

    def get_success_url(self):
        return reverse('index')

    # def form_valid(self, form):
    #     print("++++++", self.request.user, "=======", post = get_object_or_404(Post,  pk=self.kwargs.get('pk')))
    #     form.instance.author = self.request.user
    #     form.instance.post = get_object_or_404(Post,  pk=self.kwargs.get('pk'))
        
    #     return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        liked_by = self.request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            mark = form.cleaned_data.get('mark')
            if not Like.objects.filter(post=post, liked_by=liked_by, mark=mark).exists():
                Like.objects.create(post=post, liked_by=liked_by, mark=mark)
        else:
            form = {'text' : 'Somthing wrong'}
        return redirect('index')



    
    

# def like(request, pk):
#     post = Post.objects.get(pk=pk)
#     liked= False
#     like = Like.objects.filter(username=request.user, post=post)
#     if like:
#         like.delete()
#     else:
#         liked = True
#         Like.objects.create(username=request.user, post=post)
#     resp = {
#         'liked':liked
#     }
#     response = json.dumps(resp)
#     return redirect('') #  redirect to any url after the object has  been liked
#     return HttpResponse(response,content_type = "application/json")
