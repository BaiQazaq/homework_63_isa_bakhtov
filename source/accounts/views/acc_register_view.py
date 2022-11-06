from django.contrib.auth import  login
from django.shortcuts import redirect
from django.views.generic import  CreateView

from accounts.forms import CustomUserCreationForm
from accounts.models import Account


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    model = Account
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # avatar = form.cleaned_data.get('avatar')
            # birthday = form.cleaned_data.get('birthday')
            # birthday = form.cleaned_data.get('birthday')
            # birthday = form.cleaned_data.get('birthday')
            # birthday = form.cleaned_data.get('birthday')
            user = form.save()
            login(request, user)
            return redirect('profile')
        context = {}
        context['form'] = form
        return self.render_to_response(context)
