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
from .models import Post
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from .forms import PostForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment
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


class PostCreateView(LoginRequiredMixin, CreateView):
    # class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")
    fields = ["title", "content"]

    def form_vaalid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    # class CommentUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDeleteView(DeleteView):
    # class CommentDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


####################
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added")
            return redirect("blog.post_detail", post_id=post.id)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form, "post": post})


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def get_queryset(self):
        # Ensure only the author of the comment can edit it
        return super().get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Your comment has been updated.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.post.id})


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"

    def get_queryset(self):
        # Ensure only the author of the comment can delete it
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.post.id})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, "blog/edit_comment.html", {"form": form})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        comment.delete()  # Deletes the comment
        return redirect("home")  # Redirect to home or wherever you'd like
    return render(request, "blog/confirm_delete.html", {"comment": comment})

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Comment  # Ensure you have this import to access your Comment model
from .forms import CommentForm  # Assuming you have a form for comments

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm  # Specify the form to use for comment updates
    template_name = 'blog/comment_form.html'  # Specify the template for rendering the form
    context_object_name = 'comment'  # Context variable for the comment instance

    def get_success_url(self):
        # Redirect to the post detail page after a successful update
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})  # Adjust based on your model structure
