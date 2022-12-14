from django import forms

from posts.models import Post, Comment, Like



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'description')

    

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
    
    
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']
        help_texts = {
                    'text' : ('Please keep mutual respect')
            }
        

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['mark']
        help_texts = {
                    'mark' : ('Like or dislike')
            }
        
        
