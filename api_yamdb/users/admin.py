from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "bio",
    )
    list_editable = ("role",)
    search_fields = (
        "username",
        "bio",
    )
    list_filter = ("role",)
    empty_value_display = "-пусто-"
