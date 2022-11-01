from django.contrib.auth import  get_user_model
from django.urls import reverse
from django.views.generic import UpdateView

from accounts.forms import  UserChangeForm


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})
