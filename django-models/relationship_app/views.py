from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    context_object_name = Library


class LoginView(CreateView):
    pass


class LogoutView(CreateView):
    next_page = reverse_lazy(login)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# Helper function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == "Admin"


# Helper function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == "Librarian"


# Helper function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == "Member"


# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")


# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")


# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")
