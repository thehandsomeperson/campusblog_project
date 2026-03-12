from .models import Post, Comment, Tag
from django import forms
class CreatePostForm(forms.ModelForm):
    new_tags = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            # add Bootstrap styling to title input
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title...'}),
            # add Bootstrap styling to content textarea
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']