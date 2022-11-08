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
            # print("Valid+"*5)
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # #password_confirm = form.cleaned_data.get('password_confirm')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # email = form.cleaned_data.get('email')
            # birthday = form.cleaned_data.get('birthday')
            # user_info = form.cleaned_data.get('user_info')
            # phone_num = form.cleaned_data.get('phone_num')
            # gender = form.cleaned_data.get('gender')
            # avatar = form.cleaned_data.get('avatar')
            # if not Account.objects.filter(username=username, email=email).exists():
            #     Account.objects.create(username=username, first_name=first_name,
            #     last_name=last_name, email=email, birthday=birthday, user_info=user_info,
            #     phone_num=phone_num, gender=gender, avatar=avatar, password=password)
            user = form.save()
            login(request, user)
            return redirect('profile')
        
        context = {}
        context['form'] = form
        return self.render_to_response(context)
