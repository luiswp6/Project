from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'summary', 'content', 'author', 'published_date')  # Incluye el campo author y otros campos necesarios

