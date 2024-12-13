from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm
from .forms import ProfileUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth import logout

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .forms import CommentForm


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form - AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


class CustomLoginView(LoginView):
    template_name = "blog/login.html"


class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
        return render(request, "blog/register.html", {"form": form})


# @login_required
# def profile(request):
#     user = get_object_or_404(User, pk =request.user.pk)
#     if request.method == "POST":
#         user.email = request.PoST.get("email")
#         user.save()
#         return redirect("profile")
#     return render(request, "blog/profile.html", {"user:user"})


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.savae()
            return redirect("profile")
        else:
            form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, "blog/profile.html", {"form": form})


# List View for all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/posy_list.html"
    context_object_name = "posts"


# DetailView for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return self.get(self.request, *args, **kwargs)
        return self.render_to_response({"form": form})


# CreateView for creating new posts


# class PostCreateView(LoginRequiredMixin, CreateView):
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")
    fields = ["title", "content"]

    def form_vaalid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class PostUpdateView(UpdateView):
class CommentUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


# class PostDeleteView(DeleteView):
class CommentDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
