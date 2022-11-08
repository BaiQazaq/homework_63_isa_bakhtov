from django import forms

from posts.models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'description')

    

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')