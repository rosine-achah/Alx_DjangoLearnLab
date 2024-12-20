from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from .models import Comment, Tag
from taggit.models import Tag
from taggit.forms import TagField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget())

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].queryset = Tag.objects.all()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your comment here....",
                    "rows": 3,
                }
            ),
        }
        labels = {
            "content": "",
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
