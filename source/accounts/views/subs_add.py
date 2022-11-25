from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from accounts.forms import SubsForm
from accounts.models import Account, Subs


class SubsAddView (LoginRequiredMixin, CreateView):
    form_class = SubsForm
    
    
    def post(self, request, *args, **kwargs):
        bloger = get_object_or_404(Account, pk=kwargs.get('pk'))
        subscriber = self.request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            mark = form.cleaned_data.get('mark')
            if not Subs.objects.filter(bloger=bloger, subscriber=subscriber, mark=mark).exists():
                Subs.objects.create(abloger=bloger, subscriber=subscriber, mark=mark)
        else:
            form = {'text' : 'Somthing wrong with subscription'}
        return redirect('profiles_list')
    
    