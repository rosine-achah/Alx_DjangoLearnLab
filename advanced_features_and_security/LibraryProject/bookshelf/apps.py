from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookshelf"


# using the Django's Group and Permission models to create groups and assign permissions programmatically.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Article


def create_groups():
    # Define groups
    viewers_group, created = Group.objects.get_or_create(name="Viewers")
    editors_group, created = Group.objects.get_or_create(name="Editors")
    admins_group, created = Group.objects.get_or_create(name="Admins")

    # Get permissions
    article_content_type = ContentType.objects.get_for_model(Article)

    can_view_permission = Permission.objects.get(
        codename="can_view", content_type=article_content_type
    )
    can_create_permission = Permission.objects.get(
        codename="can_create", content_type=article_content_type
    )
    can_edit_permission = Permission.objects.get(
        codename="can_edit", content_type=article_content_type
    )
    can_delete_permission = Permission.objects.get(
        codename="can_delete", content_type=article_content_type
    )

    # Assign permissions to groups
    viewers_group.permissions.add(can_view_permission)
    editors_group.permissions.add(
        can_view_permission, can_create_permission, can_edit_permission
    )
    admins_group.permissions.add(
        can_view_permission,
        can_create_permission,
        can_edit_permission,
        can_delete_permission,
    )
