from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("email", "password", "username")}),
        ("Personal info", {"fields": ("date_of_birth", "profile_photo")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_join")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "date_of_birth",
                    "profile_photo",
                ),
            },
        ),
    )

    list_display = ("email", "username", "date_of_birth", "is_staff")
    search_fields = ("email", "date_of_birth")

    ordering = ("email",)


admin.site.register(CustomUserAdmin, CustomUser)
